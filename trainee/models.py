from django.db import models



class Track(models.Model):
    name = models.CharField(max_length = 25);
    id = models.AutoField(primary_key=True);
    
    
    def __str__(self):
        return self.name;

class Trainee(models.Model):
    name = models.CharField(max_length = 50)
    id = models.AutoField(primary_key=True);
    track = models.ForeignKey(Track, on_delete = models.CASCADE, default=None)
    password = models.CharField(max_length = 15);

