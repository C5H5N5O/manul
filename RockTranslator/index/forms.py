from tkinter import Widget
from django.forms import ModelForm, TextInput
from .models import Massage

class MassageForm(ModelForm):
    class Meta:
        model = Massage

        fields = ['context']

        widgets = {
            'context': TextInput(
                attrs={
                    'class': 'form-control',
                    'id'   : 'input'
                })
        }