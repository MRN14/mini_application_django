from django.db import models

# class Manufacturer(models.Model):
#     name = models.CharField()

class Products(models.Model):
    ref = models.CharField(max_length=48, primary_key=True),
    name = models.CharField(),
    stock = models.PositiveBigIntegerField(default=0)
    # manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)

