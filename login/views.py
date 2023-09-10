from django.http import HttpResponse
from django.shortcuts import render




def login(request):
    print(request.POST);
    res = HttpResponse();
    return render(request, 'login.html');



def register(request):
    print(request.POST);
    res = HttpResponse();
    return render(request, 'register.html');
