from django.contrib import admin
from .models import Project, StatusCode, UserProfile, TeamName, Role, Task, Comment

# Register your models here.
admin.site.register(Project)
admin.site.register(StatusCode)
admin.site.register(UserProfile)
admin.site.register(TeamName)
admin.site.register(Role)
admin.site.register(Task)
admin.site.register(Comment)
