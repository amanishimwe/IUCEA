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
from rest_framework.renderers import TemplateHTMLRenderer


#def university_count(request):
#    universityCount = University.objects.all().count()
#    template = loader.get_template('apims/index.html')
 #   context = {'universityCount': universityCount}
  #  return HttpResponse(template.render(context, request))

class CountView(TemplateView):
    template_name = 'apims/index.html'
    def get_context_data(self, **kwargs):
        context = super(CountView,self).get_context_data(**kwargs)
        context['universityCount'] = University.objects.all().count()
        context['programCount'] = Program.objects.all().count()
        context['undergradCount'] = Program.objects.filter(program_level ='Bachelors').count()
        context['postgradCount'] =Program.objects.filter(Q(program_level ='Masters') | Q(program_level ='Post Graduate Diploma') | Q(program_level ='Doctorate')).count()
        return context


def country_university_view(request):

    return render(request,'apims/index.html',{})

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format = None):
        universities = list(University.objects.values())
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
            "universities": universities,

        }
        return Response(data)


class UniversitiesDetails(TemplateView):
    template_name = 'apims/universities.html'
    def get_context_data(self, **kwargs):
        context = super(UniversitiesDetails, self).get_context_data(**kwargs)
        context['universities'] = University.objects.all()[:10]
        return context


