from django.urls import path
from .import views



urlpatterns = [
    path('', views.home, name='accueil'),
    path('accueil', views.home, name='accueil'),
    path('propos', views.propos, name='propos'),
    path('contact', views.contact, name='contact'),
    path('services', views.service, name='services'),
    ]