from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def propos(request):
    return render(request, 'propos.html')


def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def transport(request):
    return render(request, 'transport.html')

def transit(request):
    return render(request, 'transit.html')

def entretien(request):
    return render(request, 'entretien.html')

def garage(request):
    return render(request, 'garage.html')

def assistance(request):
    return render(request, 'assistance.html')

def piece(request):
    return render(request, 'piece.html')