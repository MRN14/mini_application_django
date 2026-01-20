from django.shortcuts import render
from magasin.models import Product

def home(request):
    
    return render(request, "magasin/index.html")

def list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "magasin/products/list.html", context)