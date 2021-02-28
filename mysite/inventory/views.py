from django.shortcuts import render
from .forms import BarcodeForm
from .models import Item
from pyzbar import pyzbar
from django.db.models import F
from PIL import Image
import cv2

def add_inventory_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = BarcodeForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the current instance object to display in the template
            form.save()
            img_obj = form.instance
            #decode barcode
            pyzbar_decoded = pyzbar.decode(Image.open(img_obj.image))
            barcode_decoded = pyzbar_decoded[0].data.decode()
            item = Item.objects.filter(barcode=barcode_decoded)
            if not item:
                return render(request, 'inputbarcode.html', {'form': form,\
                 'barcode_decoded': barcode_decoded, 'itemno': "This Item doesnt' exist",\
                     'item_type': "error"})
            item.update(amount=F('amount')+1)
            item_no = Item.objects.get(barcode=barcode_decoded).amount
            item_type = Item.objects.get(barcode=barcode_decoded).Name

            return render(request, 'inputbarcode.html', {'form': form,\
                 'barcode_decoded': barcode_decoded, 'itemno': item_no, 'item_type': item_type})
    else:
        form = BarcodeForm()
    return render(request, 'inputbarcode.html', {'form': form})

def sell_inventory_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = BarcodeForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the current instance object to display in the template
            form.save()
            img_obj = form.instance
            #decode barcode
            pyzbar_decoded = pyzbar.decode(Image.open(img_obj.image))
            barcode_decoded = pyzbar_decoded[0].data.decode()
            item = Item.objects.filter(barcode=barcode_decoded)
            if not item:
                return render(request, 'inputbarcode.html', {'form': form,\
                 'barcode_decoded': barcode_decoded, 'itemno': "This Item doesnt' exist",\
                     'item_type': "error"})
            if item[0].amount==0:
                item = Item.objects.get(barcode=barcode_decoded)
                item_type = item.Name
                email = item.supplier_email
                return render(request, 'inputbarcode.html', {'form': form,\
                 'barcode_decoded': barcode_decoded, 'itemno': 0,\
                     'item_type': item_type, 'email': email})
            item.update(amount=F('amount')-1)
            item_no = Item.objects.get(barcode=barcode_decoded).amount
            item_type = Item.objects.get(barcode=barcode_decoded).Name

            if item[0].amount==0:
                item = Item.objects.get(barcode=barcode_decoded)
                item_type = item.Name
                email = item.supplier_email
                return render(request, 'inputbarcode.html', {'form': form,\
                 'barcode_decoded': barcode_decoded, 'itemno': "You don't have any more of this item",\
                     'item_type': item_type, 'email': email})
            return render(request, 'inputbarcode.html', {'form': form,\
                 'barcode_decoded': barcode_decoded, 'itemno': item_no, 'item_type': item_type})
    else:
        form = BarcodeForm()
    return render(request, 'inputbarcode.html', {'form': form})

def info_vids(request):
    return render(request, 'youtubevids.html')