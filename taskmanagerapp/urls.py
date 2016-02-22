from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.project_list, name='project_list'),
    url(r'^project/(?P<pk>[0-9]+)/$', views.project_detail, name='project_detail'),
    url(r'^project/new/$', views.new_project, name='new_project'),
    url(r'^project/(?P<pk>[0-9]+)/edit/$', views.project_edit, name='project_edit'),
    url(r'^accounts/register/$', views.register, name='register'),
    url('^login/', auth_views.login),
    url('^logout/', auth_views.logout),
    url(r'^task/new/$', views.new_task, name='new_task'),
    url(r'^task/(?P<pk>[0-9]+)/$', views.task_detail, name='task_detail'),
    url(r'^task/(?P<pk>[0-9]+)/edit/$', views.task_edit, name='task_edit'),
    url(r'^project/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_project, name='add_comment_to_project'),

]
