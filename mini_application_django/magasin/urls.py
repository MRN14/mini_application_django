from django.urls import include, path
from magasin import views


app_name = "magasin"
urlpatterns =  [
    path('', views.home ),
    path('', include('magasin.products-urls'))
]

