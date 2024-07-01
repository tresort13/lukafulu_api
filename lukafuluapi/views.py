
from django.http import HttpResponse
from .models import Decharges
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DechargeSerializer
from datetime import datetime
# Create your views here.
# Register API

        
def welcom(request):
    return HttpResponse('WELCOM TO LUKAFULU  API RESOURCES')

@api_view(['POST'])   
def dechargesInformationsEnvoi(request): 
        localisation_decharge= request.data['localisation_decharge']
        description_decharge= request.data['description_decharge']
        dimensions_decharge= request.data['dimensions_decharge']
        dechets_observes= request.data['dechet_observer']
        nuisances_observees = request.data['nuisances_observer']
        description_situation= request.data['description_situation']
        observation= request.data['observation']
        photo_decharge= request.data['photo']
        geolocalisation_longitude= request.data['longitude']
        geolocalisation_latitude= request.data['latitude']
        geolocalisation_altitude = request.data['altitude']
        geolocalisation_altitudeAccuracy = request.data['altitudeAccuracy']
        geolocalisation_accuracy = request.data['accuracy']
        geolocalisation_speed= request.data['speed']
        geolocalisation_timestamp= request.data['timestamp']
        
        
        
        serializer = DechargeSerializer(data={'localisation_decharge': localisation_decharge,'description_decharge' : description_decharge,'dimension_decharge' : dimensions_decharge,'dechets_observes':dechets_observes,'nuisances_observees' : nuisances_observees,'description_situation' : description_situation,'observation' : observation,'photo_decharge':photo_decharge,'geolocalisation_longitude' : geolocalisation_longitude,'geolocalisation_latitude':geolocalisation_latitude,'geolocalisation_altitude' : geolocalisation_altitude, 'geolocalisation_altitudeAccuracy' : geolocalisation_altitudeAccuracy,'geolocalisation_accuracy':geolocalisation_accuracy,'geolocalisation_speed': geolocalisation_speed,'timestamp':geolocalisation_timestamp,'data_operation':str(datetime.now().date()),'date_heure_operation':str(datetime.now()),'month_year_operation':str(datetime.now().year)+"-"+str(datetime.now().month)})
        if serializer.is_valid() :
          serializer.save()
          return Response(serializer.data)
        return Response('',status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])   
def dechargesInformations(request): 
    try:
        envoies_data = Decharges.objects.all()
    except envoies_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method =='GET':
            serializer = DechargeSerializer(envoies_data,many=True)
            return Response(serializer.data)