from django import forms
from .models import Barcode


class BarcodeForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Barcode
        fields = ('image',)