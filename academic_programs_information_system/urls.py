from django.urls import path
from .views import ChartData

from . import views

urlpatterns = [
    path('', views.university_count, name = 'university_count'),
    path('api/chart/data/' , ChartData.as_view()),

]