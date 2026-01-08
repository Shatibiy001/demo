from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User  
from . models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from project.models import Project
from .forms import CustomUserCreationForm
from .forms import ProfileForm
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def loginPage(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
           messages.error(request, 'user does not exit')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'user name or password is not correct')
            
    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.error(request, 'user logged out')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()  # ✅ signal creates Profile automatically

            messages.success(request, 'Your account has been successfully created!')

            login(request, user)
            return redirect('profiles')

        else:
            messages.error(
                request,
                'An error occurred during registration. Please check the form fields.'
            )

    context = {
        'page': page,
        'form': form,
    }

    return render(request, 'users/login.html', context)


def aboutus(request):
    context = {
        'page_title': 'About This Platform',
    }
    return render(request, 'users/about.html', context)

    

@login_required(login_url="login")
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles' : profiles}
    messages.error(request, 'login sucessful')
    return render (request, 'users/profile.html', context)

@login_required(login_url="login")
def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    projects = Project.objects.filter(owner=profile)
    context = {'profile': profile, 'projects': projects}
    return render(request, 'users/user_profile.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = None
    projects = []

    try:
        profile = request.user.profile
        projects = profile.project_set.all()   # only run if profile exists
    except (AttributeError, ObjectDoesNotExist):
        # Profile doesn't exist yet for this user
        # You can handle this case (e.g. show message, redirect to create profile, etc.)
        pass  # for now we just set to None/empty

    context = {
        'profile': profile,
        'projects': projects,
        'user': request.user,  # useful fallback
    }

    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  
            return redirect('account')  # or your profile page
    else:
        # Pre-fill the input with current skills
        initial_skills = ', '.join(profile.skill_set.values_list('name', flat=True))
        form = ProfileForm(instance=profile, initial={'new_skills': initial_skills})

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'users/edit-account.html', context)