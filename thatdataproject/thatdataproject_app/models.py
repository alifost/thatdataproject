from django.db import models

# Create your models here.

class PoliceShootings(models.Model):
    id = models.IntegerField(primary_key=True)
    models.TextField()
    name = models.TextField()
    date = models.TextField()
    manner_of_death = models.TextField()
    armed = models.TextField()
    age = models.IntegerField()
    gender = models.TextField()
    race = models.TextField()
    city = models.TextField()
    state = models.TextField()
    signs_of_mental_illness = models.IntegerField()
    threat_level = models.TextField()
    flee = models.TextField()
    body_camera = models.IntegerField()
