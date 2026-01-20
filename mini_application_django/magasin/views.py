from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "magasin/index.html")

def list(request):
    return render(request, "magasin/products/list.html")