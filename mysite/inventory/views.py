from django.shortcuts import render
from .forms import BarcodeForm
from pyzbar import pyzbar
from PIL import Image
import cv2

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = BarcodeForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the current instance object to display in the template
            form.save()
            img_obj = form.instance
            print(img_obj.image)
            barcode_decoded = pyzbar.decode(Image.open(img_obj.image))
            print(barcode_decoded)
            return render(request, 'inputbarcode.html', {'form': form,\
                 'barcode_decoded': barcode_decoded, 'img_obj': img_obj})
    else:
        form = BarcodeForm()
    return render(request, 'inputbarcode.html', {'form': form})