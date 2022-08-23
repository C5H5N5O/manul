from concurrent.futures import thread
from tkinter import dialog
from django.shortcuts import render
from django.http import HttpResponse

from index import set_db_worker_started
from .models import Rock, Massage
from .forms import MassageForm

import random, time, threading

def preloader(request):
    return render(request, 'main/preloader.html')


def index(request):
    
    error = ""
    if request.method == "POST":
        form = MassageForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = ".........."


    from . import db_updater_working

    if not db_updater_working:
        Rock.objects.filter(name="Valentin").update(happiness_index=100)

        def db_updater():
            while True:
                time.sleep(86400)
                Rock.objects.filter(name="Valentin").update(happiness_index=
                    Rock.objects.all()[0].happiness_index - random.randint(14, 29))

        threading.Thread(target=db_updater, ).start()

        print("db_updater is started")
        set_db_worker_started()

    Valentin    = Rock.objects.all()[0]

    hunger      = Valentin.hunger_index
    happiness   = Valentin.happiness_index
    health      = random.randint(87, 92)
    
    form = MassageForm()

    chat = Massage.objects.all()
    if len(chat) > 9:
        chat = chat[len(chat)-9:len(chat)]

    return render(request, "main/main/index.html",  
    {   
        'hunger_index'   : hunger,
        'happiness_index': happiness, 
        'health_index'   : health,
        'form'           : form,
        'error'          : error,
        'chat'           : chat
    })


def flappy(request):
    Rock.objects.filter(name="Valentin").update(happiness_index=100)

    return render(request, "main/flappy_bird/index.html")
