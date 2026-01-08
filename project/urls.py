from django.urls import path
from . import views 

urlpatterns = [
    path('project', views.projects, name='projects'),
    path('project/<uuid:pk>/', views.project_detail, name='project'), 
    path('createproject/', views.createproject, name="createproject"),
    path('updateproject/<uuid:pk>>/', views.updateproject, name='updateproject'),
    path('deleteproject/<uuid:pk>>/', views.deleteproject, name='deleteproject'),
    path('', views.all_projects, name='all_projects'),

]

