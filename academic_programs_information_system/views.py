import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from django.views.generic import TemplateView

def university_count(request):
    universityCount = University.objects.all().count()
    template = loader.get_template('apims/index.html')
    context = {'universityCount': universityCount}
    return HttpResponse(template.render(context, request))

def country_university_view(request):

    return render(request,'apims/index.html',{})
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format = None):
        member_universities_count = University.objects.filter(
            Q(iucea_membership='full member') | Q(iucea_membership='associate')).count()
        chartered_universities_count=University.objects.filter(level_of_progression='chartered').count()
        public_universities_count = University.objects.filter(type_of_establishment='public').count()
        private_universities_count =University.objects.filter(type_of_establishment='private').count()

        labels =["Member Universities","Chartered Universities","Public Universities","Private Universities"]
        default_items =[member_universities_count,chartered_universities_count ,public_universities_count,private_universities_count]
        data = {

            "labels" :labels,
            "default" : default_items,

        }
        return Response(data)

class CharteredUniversitiesDetailsView(TemplateView):
    template_name = 'apims/chartered.html'