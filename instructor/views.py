from django.http import HttpResponse
from django.shortcuts import render
from .models import Instructor;


def homepage(request):
    return render(request, 'base.html');

def insert(request):
    obj = request.POST;
    if request.method == 'GET':
        return render(request, 'register.html');    
    instructor = Instructor();
    instructor.name = obj['username']
    instructor.password = obj['password'];
    instructor.save();
    return render(request, 'register.html');


def login(request):
    obj = request.POST;
    if request.method == 'GET':
        return render(request, 'login.html')
    
    instructor = Instructor.objects.get(name = obj['username'], password = obj['password']);
    
    if instructor is None:
        return render(request, 'login.html')

    return render(request, 'base.html');
        

def delete(request):
    res = HttpResponse()
    res.write("Deleting an instructor");
    return res;


def update(request):
    res = HttpResponse();
    res.write("Updating an instructor");
    return res;


def show(request):
    objects = Instructor.objects.all();
    context = {'Instructors': objects};
    return render(request, 'listingAllInstructors.html', context)


