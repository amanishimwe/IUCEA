from django.urls import path
from .views import ChartData,UniversitiesDetails,CountView, ProgramDetails
from django.views.generic import TemplateView

from . import views

app_name = 'academic_programs_information_system'

urlpatterns = [
    #path('', views.university_count, name = 'university_count'),

    path('', CountView.as_view(template_name = 'apims/index.html'), name ='home' ),
    path('api/chart/data/' , ChartData.as_view()),
    path('universities/', UniversitiesDetails.as_view(template_name = 'apims/universities.html'), name = 'universitiesDetails'),
    path('programs/',ProgramDetails.as_view(template_name = 'apims/programs.html'), name = 'programDetails'),
]