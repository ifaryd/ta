from django.urls import path
from .import views



urlpatterns = [
    path('', views.home, name='accueil'),
    path('accueil', views.home, name='accueil'),
    path('propos', views.propos, name='propos'),
    path('contact', views.contact, name='contact'),
    path('services', views.service, name='services'),
    path('transport', views.transport, name='transport'),
    path('transit', views.transit, name='transit'),
    path('entretien', views.entretien, name='entretien'),
    path('garage', views.garage, name='garage'),
    path('piece', views.piece, name='piece'),
    path('assistance', views.assistance, name='assistance'),
    ]