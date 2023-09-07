from django.http import HttpResponse
from django.shortcuts import render



def insert(request):
    res = HttpResponse();
    res.write("Inserting an instructor");
    return res;




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