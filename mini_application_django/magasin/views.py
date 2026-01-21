from django.shortcuts import render
from magasin.models import Product

def home(request):
    context = {
        "title": "Magasin DGA - Accueil"
    }
    return render(request, "magasin/index.html", context)

def list(request):
    products = Product.objects.all()
    count = Product.objects.count()
    context = {
        "products": products,
        "count" : count,
        "title": "magasin DGA - liste produits"
    }
    return render(request, "magasin/products/list.html", context)