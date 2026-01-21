from django.db import models

class Manufacturer(models.Model):
    name = models.CharField()

    def __str__(self):
        return f'{ self.name }'

class Product(models.Model):
    ref = models.CharField(max_length=48, primary_key=True)
    name = models.CharField(max_length=48)
    stock = models.PositiveBigIntegerField(default=0)

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True )
    

    # amélioration possible : création de catégories
    # class Category(models.TextChoices):
    #     ELECTRONIC = "electronic"

    def __str__(self):
        return f'{ self.ref }'

