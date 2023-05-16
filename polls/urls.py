from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('sobre/', views.sobre, name = 'sobre'),
=======

from . import views

urlpatterns = [
    path('', views.index, name='index'),
>>>>>>> ecd1c1aa8bde16f553ba2cabf0dbd9118c19ea56
]