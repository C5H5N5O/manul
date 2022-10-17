from contextlib import redirect_stdout
from operator import indexOf
from zoneinfo import available_timezones
from django.shortcuts import render, redirect, HttpResponseRedirect

from index import set_db_worker_started
from .models import Rock, Massage, User
from .forms import MassageForm, ChoseRockForm

import random, time, threading
from django.views.decorators.csrf import csrf_exempt

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

    user = User.objects.all()[0]
    curent_rock = Rock.objects.all()[user.curent_rock]

    if not db_updater_working:
        Rock.objects.filter(name=curent_rock.name).update(happiness_index=100)

        def db_updater():
            while True:
                time.sleep(86400)
                curent_rock.update(happiness_index=
                    curent_rock.happiness_index - random.randint(14, 29))

        threading.Thread(target=db_updater, ).start()

        print("db_updater is started")
        set_db_worker_started()

    hunger    = curent_rock.hunger_index
    happiness = curent_rock.happiness_index
    health    = random.randint(87, 92)
    img       = curent_rock.scin

    form = MassageForm()
    chose_form = ChoseRockForm()

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
        'chat'           : chat,
        'img'            : img,
        'choise_form'    : chose_form,
        'user'           : user
    })  

@csrf_exempt
def change_rock(request):
    if request.method == "POST":
        scin = request.POST.get("curent_skin")
        print(scin)
        rocks_images = [
            "https://cdn.discordapp.com/attachments/432562983776944150/1009577884828045352/11.png",
            "https://cdn.discordapp.com/attachments/432562983776944150/1009577883666227240/14.png",
            "https://cdn.discordapp.com/attachments/432562983776944150/1009574239893995571/1.png",
            "https://cdn.discordapp.com/attachments/432562983776944150/1009574238681841664/9.png",
            "https://cdn.discordapp.com/attachments/432562983776944150/1009574236261720074/3.png",
            "https://cdn.discordapp.com/attachments/432562983776944150/1009574236815376394/5.png",
            "https://cdn.discordapp.com/attachments/432562983776944150/1009574238082048090/8.png",
            "https://cdn.discordapp.com/attachments/432562983776944150/1009574239310991390/4.png",
            "https://cdn.discordapp.com/attachments/432562983776944150/1009574239893995571/1.png"
        ]
        Rock.objects.filter(name="Valentin").update(scin=int(scin))

    return HttpResponseRedirect('/main/')

