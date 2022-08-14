from django.urls import path
from . import views

urlpatterns = [
    path('', views.preloader),
    path('main/', views.index),
    path('main/flappy_rock', views.flappy)
]
