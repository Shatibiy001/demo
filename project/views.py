from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import ProjectForm 
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