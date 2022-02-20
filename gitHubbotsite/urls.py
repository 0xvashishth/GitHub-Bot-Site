"""gitHubbotsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from botsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_users/',views.list_users,name='list_users'),
    path('create/',views.create_users,name='create_users'),
    path('<id>/',views.detail_users,name='detail_users'),
    path('<id>/update',views.update_users,name='update_users'),
    path('<id>/delete',views.delete_users,name='delete_users'),
    path('file_path',views.get_path,name='show_path'),
    path('',views.index,name='index'),
    path('registered',views.registered,name='registered'),
    path('login',views.login,name='login'),
]
