from django.db import models
from django.utils import timezone

# Create your models here.
class StatusCode(models.Model):
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
    author = models.ForeignKey('auth.User', related_name='author')
    created_at = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(default=timezone.now)
    assigned_users = models.ManyToManyField('auth.User', related_name='assigned_users')
    project_status = models.ForeignKey(StatusCode, default=1)
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
