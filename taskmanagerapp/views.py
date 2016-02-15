from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Project
from .forms import ProjectForm
from django.shortcuts import redirect

# Create your views here.
def project_list(request):
    projects = Project.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'taskmanagerapp/project_list.html', {'projects': projects})

def project_detail(request, pk):
    proj = get_object_or_404(Project, pk=pk)
    return render(request, 'taskmanagerapp/project_detail.html', {'proj': proj})

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

def project_edit(request, pk):
    proj2 = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=proj2)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('taskmanagerapp.views.project_detail',pk=project.pk)
    else:
        form = ProjectForm(instance=proj2)
    return render(request, 'taskmanagerapp/project_edit.html', {'form': form})
