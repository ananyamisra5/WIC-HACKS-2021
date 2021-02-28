from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=120)
    barcode = models.IntegerField(unique=True)

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)

class Barcode(models.Model):
    image = models.ImageField(upload_to='images')
