from django.urls import path
from .views import *
from django.views.generic import TemplateView

from . import views

app_name = 'academic_programs_information_system'

urlpatterns = [
    # path('', views.university_count, name = 'university_count'),

    path('', CountView.as_view(template_name='apims/index.html'), name='home'),
    path('api/chart/data/', ChartData.as_view()),
    path('universities/', UniversitiesDetails.as_view(template_name='apims/universities.html'),
         name='universitiesDetails'),
    path('programs/', ProgramDetails.as_view(template_name='apims/programs.html'), name='programDetails'),
    path('burundi/', BurundiData.as_view(template_name='apims/burundi.html'), name='burundiData'),
    path('kenya/', KenyaData.as_view(template_name='apims/kenya.html'), name='kenyaData'),
    path('rwanda/', RwandaData.as_view(template_name='apims/rwanda.html'), name='rwandaData'),
    path('south_sudan/', SudanData.as_view(template_name='apims/sudan.html'), name='sudanData'),
    path('tanzania/', TanzaniaData.as_view(template_name='apims/tanzania.html'), name='tanzaniaData'),
    path('uganda/', UgandaData.as_view(template_name='apims/uganda.html'), name='ugandaData'),
]
