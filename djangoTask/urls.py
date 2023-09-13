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
import login.views;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', instructor.views.homepage, name='home'),
    path('trainee/insert', trainee.views.insert, name = 'insertTrainee'),
    path('trainee/update/<int:id>', trainee.views.update, name = 'updateTrainee'),
    path('trainee/delete/<int:id>', trainee.views.delete, name = 'deleteTrainee'),
    path('trainee/show', trainee.views.show, name = 'showTrainee'),
    
    
    path('instructor/insert', instructor.views.insert, name = 'insertInstructor'),
    path('instructor/update', instructor.views.update, name = 'updateInstructor'),
    path('instructor/delete', instructor.views.delete, name = 'deleteInstructor'),
    path('instructor/show', instructor.views.show, name = 'showInstructor'),
    
    
]
