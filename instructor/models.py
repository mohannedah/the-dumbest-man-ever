from django.db import models




class Instructor(models.Model):
    name = models.CharField(max_length = 50)
    id = models.AutoField(primary_key=True);
    password = models.CharField(max_length = 15);
