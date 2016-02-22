from django import forms
from .models import Project, UserProfile, Task, Comment
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields =('title', 'assigned_users', 'project_status', 'deadline', 'priority', 'description',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'team', 'role', 'photo',)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('project', 'title', 'task_status', 'start_date', 'deadline', 'description',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('description',)
