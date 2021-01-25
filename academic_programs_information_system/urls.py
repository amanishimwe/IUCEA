from django.urls import path
from .views import ChartData
from django.views.generic import TemplateView

from . import views

app_name = 'academic_programs_information_system'

urlpatterns = [
    path('', views.university_count, name = 'university_count'),
    path('api/chart/data/' , ChartData.as_view()),
    path('chartered/', TemplateView.as_view(template_name = 'apims/chartered.html'), name = 'chartered'),

]