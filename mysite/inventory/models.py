from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=120)
    barcode = models.CharField(max_length=120, unique=True)
    amount = models.IntegerField()
    supplier_email = models.EmailField(max_length=254)
    buying_price = models.DecimalField(max_digits=10,decimal_places=2)
    selling_price = models.DecimalField(max_digits=10,decimal_places=2)

class Finance(models.Model):
    id = models.AutoField(primary_key=True)
    money = models.DecimalField(max_digits=10,decimal_places=2)

class Barcode(models.Model):
    image = models.ImageField(upload_to='images')
