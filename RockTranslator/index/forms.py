from secrets import choice
from tkinter import Widget
from django.forms import ModelForm, TextInput
from .models import Massage, User

from django import forms

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



class ChoseRockForm(forms.Form):

    available_rocks = [rock for rock in User.objects.all()[0].available_rocks]
    scins = []
    for _ in range(len(available_rocks)):
        scins.append(min(available_rocks))
        available_rocks.pop(available_rocks.index(min(available_rocks)))

    
    ch = []
    for i, j in enumerate(scins):
        ch.append((i, j))

    change = (i for i in ch)

    
    скин = forms.ChoiceField (
        choices=change
    )
