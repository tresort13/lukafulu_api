from .models import Decharges
from rest_framework import serializers
from django.contrib.auth.models import User



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email','is_superuser','last_login','date_joined')

    
# Envoies_data Serializer
class DechargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decharges
        fields = ('id', 'localisation_decharge','description_decharge','dimension_decharge','dechets_observes','nuisances_observees','description_situation',
                  'observation','photo_decharge','geolocalisation_longitude',
                 'geolocalisation_latitude','geolocalisation_altitude','geolocalisation_altitudeAccuracy','geolocalisation_accuracy','geolocalisation_speed','timestamp','data_operation','date_heure_operation','month_year_operation')




        
