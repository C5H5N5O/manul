from django.shortcuts import render


from index import set_db_worker_started
from .models import Rock, User
import random, time, threading


def preloader(request):
    return render(request, 'main/preloader.html')


def index(request):

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

    return render(request, "main/main/index.html",
    {   
        'hunger_index'   : hunger,
        'happiness_index': happiness, 
        'health_index'   : health 
    })


def flappy(request):
 
    Rock.objects.all()[User.objects.all[0]].update(happiness_index=100)

    return render(request, "main/flappy_bird/index.html")