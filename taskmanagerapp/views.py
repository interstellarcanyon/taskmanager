from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Project, Task, Comment
from .forms import ProjectForm, UserForm, UserProfileForm, TaskForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def project_list(request):
    projects = Project.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'taskmanagerapp/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    proj = get_object_or_404(Project, pk=pk)
    return render(request, 'taskmanagerapp/project_detail.html', {'proj': proj})

@login_required
def task_detail(request, pk):
    task= get_object_or_404(Task, pk=pk)
    return render(request, 'taskmanagerapp/task_detail.html', {'task': task})

@login_required
def new_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('taskmanagerapp.views.project_detail',pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'taskmanagerapp/project_edit.html', {'form': form})

@login_required
def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('taskmanagerapp.views.project_list')
    else:
        form = TaskForm()
    return render(request, 'taskmanagerapp/task_edit.html', {'form': form})

@login_required
def add_comment_to_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.project=project
            comment.save()
            return redirect('taskmanagerapp.views.project_detail', pk=project.pk)
    else:
        form = CommentForm()
    return render(request, 'taskmanagerapp/add_comment_to_project.html', {'form': form})

@login_required
def project_edit(request, pk):
    proj2 = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=proj2)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            form.save_m2m()
            return redirect('taskmanagerapp.views.project_detail',pk=project.pk)
    else:
        form = ProjectForm(instance=proj2)
    return render(request, 'taskmanagerapp/project_edit.html', {'form': form})

@login_required
def task_edit(request, pk):
    task2 = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task2)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            form.save_m2m()
            return redirect('taskmanagerapp.views.task_detail',pk=task.pk)
    else:
        form = TaskForm(instance=task2)
    return render(request, 'taskmanagerapp/task_edit.html', {'form': form})

def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST, prefix='user')
        upf = UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return redirect('taskmanagerapp.views.project_list')
    else:
        uf = UserForm()
        upf = UserProfileForm()
    return render(request, 'taskmanagerapp/register.html', {'uf': uf, 'upf': upf})
