from django.urls import path
from magasin import views

app_name = "product"
urlpatterns = [
    path('produits/', views.list, name="list"),
    path('produit/<str:ref>/', views.detail, name="detail"),
]