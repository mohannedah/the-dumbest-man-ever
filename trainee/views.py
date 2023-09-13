from django.http import HttpResponse
from django.shortcuts import render
from .models import Trainee, Track;


def insert(request):
    if request.method == "GET":
        tracks = Track.objects.all();
        return render(request, 'insertTrainee.html', {'tracks': tracks});
    
    obj = request.POST;
    trainee = Trainee();
    
    trainee.name = obj["name"];
    trainee.track = Track.objects.get(id = obj["track"]);
    trainee.save();
    return render(request, 'base.html');




def delete(request, id):
    Trainee.objects.get(id=id).delete();
    trainees = Trainee.objects.all();
    return render(request, 'listTrainees.html', {'trainees': trainees});


def update(request, id):
    trainee =  Trainee.objects.get(id = id);
    tracks = Track.objects.all();
    print([trainee.track])
    if request.method == "GET":
        return render(request, 'updateTrainee.html', {"trainee": trainee, "tracks": tracks});
    obj = request.POST;
    trainee.name = obj["name"];
    trainee.track = Track.objects.get(id = obj["track"]);
    trainee.save(); 
    return render(request, 'base.html');


def show(request):
    trainees = Trainee.objects.all();
    context = {"trainees": trainees};
    return render(request, 'listTrainees.html', context);

