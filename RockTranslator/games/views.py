from django.shortcuts import render
from index.models import Rock
# Create your views here.

def menu(request):
    return render(request, 'menu/index.html')


def flappy(request):
    Rock.objects.filter(name="Valentin").update(happiness_index=100)

    return render(request, "flappy_bird/index.html")
