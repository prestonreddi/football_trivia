"""
URL configuration for football_trivia project.

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/5.2/topics/http/urls/

Examples:

Function views
  1. Add an import:  from my_app import views
  2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views
  1. Add an import:  from other_app.views import Home
  2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf
  1. Import the include() function: from django.urls import include, path
  2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from trivia import views as trivia_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', trivia_views.home, name='home'),
    path('quiz/', trivia_views.quiz, name='quiz'),
    path('profile/', trivia_views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', include('users.urls')),  
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

]
