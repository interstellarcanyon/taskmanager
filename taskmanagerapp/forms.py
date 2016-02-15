from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields =('title', 'assigned_users', 'project_status', 'deadline', 'priority', 'description',)
