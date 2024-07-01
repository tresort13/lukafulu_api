from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
    
class Decharges(models.Model):
    localisation_decharge = models.CharField(max_length=100,default="")
    description_decharge = models.CharField(max_length=100,default="")
    dimension_decharge = models.CharField(max_length=100,default="")
    dechets_observes = models.CharField(max_length=100,default="")
    nuisances_observees = models.CharField(max_length=100,default="")
    description_situation = models.CharField(max_length=100,default="")
    observation = models.CharField(max_length=100,default="")
    photo_decharge = CloudinaryField('image')
    geolocalisation_longitude = models.CharField(max_length=100,default="")
    geolocalisation_latitude = models.CharField(max_length=100,default="")
    geolocalisation_altitude = models.CharField(max_length=100,default="")  
    geolocalisation_altitudeAccuracy = models.CharField(max_length=100,default="") 
    geolocalisation_accuracy = models.CharField(max_length=100,default="")
    geolocalisation_speed = models.CharField(max_length=100,default="")
    timestamp= models.CharField(max_length=100,default="")
    data_operation = models.CharField(max_length=50,default="")
    date_heure_operation =models.CharField(max_length=50,default="")
    month_year_operation = models.CharField(max_length=10,default="") 
   