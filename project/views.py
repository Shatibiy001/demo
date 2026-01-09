from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project, Message, User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import ProjectForm 
from django.conf import settings
# Create your views here.

# projects/views.py
def all_projects(request):
    projects = Project.objects.all().order_by('-created')
    context = {'projects': projects, 'page_title': 'All Projects'}
    return render(request, 'project/user_projects.html', context)

@login_required(login_url="login")
def projects(request):
    project_list = Project.objects.all()

    paginator = Paginator(project_list, 6)  # 6 per page
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    context = {'projects': projects}
    return render(request, 'project/projects.html', context)

@login_required(login_url="login")
def projec(request, pk):
    projectsobj = Project.objects.get(id=pk)
    #print(projectsobj.featured_image)
    tags = projectsobj.tags.all()
    return render(request, )

from django.shortcuts import render

@login_required(login_url="login")
def createproject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, "project/pr_file.html", context)

@login_required(login_url="login")
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project/project_detail.html', {'project': project})

@login_required(login_url="login")
def updateproject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, "project/pr_file.html", context)

@login_required(login_url="login")
def deleteproject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect(projects)
    context = {'object':project}
    return render(request, 'project/delete.html', context)

@csrf_protect
@login_required
def send_message_to_developer(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)

    try:
        target_owner_id = int(request.POST.get('target_owner_id'))
        project_id = request.POST.get('project_id')  # can be empty
        subject = request.POST.get('subject', '').strip()
        body = request.POST.get('message', '').strip()

        if not body:
            return JsonResponse({'status': 'error', 'message': 'Message cannot be empty'}, status=400)

        receiver = User.objects.get(id=target_owner_id)

        # Optional: check that receiver != sender
        if receiver == request.user:
            return JsonResponse({'status': 'error', 'message': 'Cannot message yourself'}, status=400)

        project = None
        if project_id:
            try:
                project = Project.objects.get(id=project_id)
            except Project.DoesNotExist:
                pass  # just continue without project

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            project=project,
            subject=subject,
            body=body
        )

        return JsonResponse({
            'status': 'success',
            'message': 'Message sent successfully!'
        })

    except User.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)