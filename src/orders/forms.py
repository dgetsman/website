from django import forms
from . import models

class CreateOrderForm(forms.Form):
    delivery_address = forms.CharField(
        required=True,
        widget=forms.Textarea
    )