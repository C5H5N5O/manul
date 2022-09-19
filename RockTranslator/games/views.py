from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponseRedirect
from index.models import Rock, User
import random


def menu(request):
    
    if request.method == "POST":
        user_get = User.objects.all()[0]
        user_set = User.objects.filter(name="manul")
        print(user_get.exp)
        if user_get.exp >= 50:

            user_set.update(exp = user_get.exp - 50)

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

            return render(request, 'menu/index.html', {"success": "true"})

        else:
            return render(request, 'menu/index.html', {"success": "false", "xp": user_get.exp})
        
    return render(request, 'menu/index.html')
    


def flappy(request):
    return render(request, "flappy_bird/index.html")


@csrf_exempt
def AddXP(request):
    print("--------------")
    if request.method == "POST":
        print("sdfsd")
        score = int(request.POST.get("score"))
        print(score)
        Rock.objects.filter(name=Rock.objects.all()[User.objects.all()[0].curent_rock]).update(happiness_index=score if score < 100 else 100)
        User.objects.filter(name="manul").update(exp=User.objects.all()[0].exp + score)

    return HttpResponseRedirect('/games/')