# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render
from dj.models import database_try
from django.http import HttpResponse

class indexPage(TemplateView):
    def get(self, request, **kwargs):
        return render(request,'index.html')

class CenterHead(TemplateView):
    def get(self, request, **kwargs):
        return render(request,'centrehead.html')

class StatePage(TemplateView):
    def get(self, request, **kwargs):
        return render(request,'statehead.html')

class ProjectPage(TemplateView):
    def get(self, request, **kwargs):
        return render(request,'projecthead.html')

class Display(TemplateView):
    def get(self, request, **kwargs):
        self.usn = request.GET['usn']
        name = request.GET['name']
        ob=database_try(artist=name,usn=self.usn)
        ob.save()
        return render(request, 'display.html',{'name':name,'usn':self.usn})

class display2(TemplateView):
    def get(self, request, **kwargs):
        all_data=database_try.objects.all()
        pic="Screenshot(2).png"
        return render(request, 'database.html', {'all_data':all_data,'pic1':pic})

def index(request):
    all_data=database_try.objects.all()
    html=''
    for a in all_data:
        url='/data/' + str(a.id) + '/'
        html += '<a href="'+url+'">'+a.artist+'</a><br>'
    return HttpResponse(html)

def detail(request,album_id):
    return HttpResponse("<h2>Details: "+str(album_id)+"</h2>")


# Create your views here.
