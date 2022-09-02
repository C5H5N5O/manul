from multiprocessing.dummy import Array
from zoneinfo import available_timezones
from django.shortcuts import render
from index.models import Rock, User

from django.contrib.postgres.fields import ArrayField

import random


def menu(request):
    
    if request.method == "POST":
        user_get = User.objects.all()[0]
        user_set = User.objects.filter(name="manul")
        available_rocks = user_get.available_rocks
        print(available_rocks)

        if len(available_rocks) == 8:
            return render(request, 'menu/index.html')
        
        new_rock = random.choice([x for x in range(8) if x not in available_rocks])

        new_available_rocks = []
        for i in available_rocks:
            new_available_rocks.append(i)
        new_available_rocks.append(new_rock)
        
        user_set.update(available_rocks=new_available_rocks)


    return render(request, 'menu/index.html')


def flappy(request):
    Rock.objects.filter(name=Rock.objects.all()[User.objects.all()[0].curent_rock]).update(happiness_index=100)
    return render(request, "flappy_bird/index.html")
