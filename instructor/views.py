from django.http import HttpResponse
from django.shortcuts import render
from .models import Instructor;


def insert(request):
    obj = request.POST;
    if request.method == 'GET':
        return render(request, 'register.html');    
    instructor = Instructor();
    instructor.name = obj['username']
    instructor.password = obj['password'];
    instructor.save();
    return render(request, 'register.html');




def delete(request):
    res = HttpResponse()
    res.write("Deleting an instructor");
    return res;


def update(request):
    res = HttpResponse();
    res.write("Updating an instructor");
    return res;


def show(request):
    res = HttpResponse();
    res.write("Showing an instructor")
    return res;


