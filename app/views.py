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