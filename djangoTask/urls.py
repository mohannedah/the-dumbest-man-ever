"""
URL configuration for djangoTask project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

import trainee.views;

import instructor.views;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trainee/insert', trainee.views.insert, name = 'insert'),
    path('trainee/update', trainee.views.update, name = 'update'),
    path('trainee/delete', trainee.views.delete, name = 'delete'),
    path('trainee/show', trainee.views.show, name = 'show'),
    
    
    path('instructor/insert', instructor.views.insert, name = 'insert'),
    path('instructor/update', instructor.views.update, name = 'update'),
    path('instructor/delete', instructor.views.delete, name = 'delete'),
    path('instructor/show', instructor.views.show, name = 'show'),
]
