from django.forms import ModelForm
from .models import Massage

class MassageForm(ModelForm):
    class Meta:
        model = Massage
        field = ['massage']