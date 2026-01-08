from django.urls import path 
from . import views

urlpatterns = [
    path('about/', views.aboutus, name='about'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user_profile"),
    path('account/', views.userAccount, name='account'),
    path('account/edit/', views.editAccount, name='edit-account'),
]

