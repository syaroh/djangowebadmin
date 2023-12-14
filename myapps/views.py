from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Home, About

def home(request):
  data = Home.objects.all()
  template = loader.get_template('home.html')
  context = {
    'contoh' : 'halo saya dari variabel',
    'produk' : data
  }
  return HttpResponse(template.render(context, request))

def myapps(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())