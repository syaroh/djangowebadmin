from django.urls import path
from . import views

urlpatterns = [
    path('myapps/', views.myapps, name='myapps'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
]