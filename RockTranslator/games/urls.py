from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu),
    path('flappy_rock', views.flappy),
    path('add_xp', views.AddXP)
]
