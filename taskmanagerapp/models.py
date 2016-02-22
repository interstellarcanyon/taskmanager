from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class StatusCode(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class TeamName(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Project(models.Model):
    PRIORITY_CHOICES = (
        ('H','High'),
        ('M', 'Medium'),
        ('L','Low'),
    )

    title = models.CharField(max_length=65)
    author = models.ForeignKey('auth.User', related_name='project_author')
    created_at = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(default=timezone.now)
    assigned_users = models.ManyToManyField('auth.User', related_name='assignedusers')
    project_status = models.ForeignKey(StatusCode, default=1)
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_number = PhoneNumberField()
    team = models.ForeignKey('taskmanagerapp.TeamName', related_name='team')
    role = models.ForeignKey('taskmanagerapp.Role', related_name='role')
    photo = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks')
    title = models.CharField(max_length=65)
    author = models.ForeignKey('auth.User', related_name='taskauthor', null=True)
    task_status = models.ForeignKey(StatusCode, default=1)
    start_date = models.DateField()
    deadline = models.DateField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class Comment(models.Model):
    project = models.ForeignKey(Project, related_name='comments')
    author = models.ForeignKey('auth.User', related_name='commentauthor', null=True)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.description
