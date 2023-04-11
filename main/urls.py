from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('uklad', views.uklad, name='uklad'),
    path('szyna', views.szyna, name='szyna'),
    path('kolor', views.kolor, name='kolor'),
    path('wymiary', views.wymiary, name='wymiary'),
    path('oprawy', views.oprawy, name='oprawy'),
    path('podsumowanie', views.podsumowanie, name='podsumowanie'),
]
