from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns = [
    path('',views.welcom, name='welcom'),
    path('api/dechargesInformationsEnvoi/',views.dechargesInformationsEnvoi,name='dechargesInformationsEnvoi'),
    path('api/dechargesInformations/',views.dechargesInformations,name='dechargesInformations'),
]

urlpatterns = format_suffix_patterns(urlpatterns)