# morsecode/urls.py
from django.urls import path
from .views import morsecode_converter

urlpatterns = [
    path('', morsecode_converter, name='morsecode_converter'),
]
