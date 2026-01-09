from django.urls import path
from . import views 
from django.http import HttpResponse
import os
from django.conf import settings

def debug_files(request):
    html = f"""
    <h1>File Debug</h1>
    <p>Debug: {settings.DEBUG}</p>
    <p>Static Root: {settings.STATIC_ROOT}</p>
    <p>Media Root: {settings.MEDIA_ROOT}</p>
    <p>Static files exist: {os.path.exists(settings.STATIC_ROOT)}</p>
    <p>Media files exist: {os.path.exists(settings.MEDIA_ROOT)}</p>
    """
    return HttpResponse(html)

urlpatterns = [
    path('debug-files/', debug_files),
    path('send-message-to-developer/', views.send_message_to_developer, name='send_message'),
    path('project', views.projects, name='projects'),
    path('project/<uuid:pk>/', views.project_detail, name='project'), 
    path('createproject/', views.createproject, name="createproject"),
    path('updateproject/<uuid:pk>>/', views.updateproject, name='updateproject'),
    path('deleteproject/<uuid:pk>>/', views.deleteproject, name='deleteproject'),
    path('', views.all_projects, name='all_projects'),

]

