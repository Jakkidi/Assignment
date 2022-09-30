from django.contrib import admin
from django.urls import path

from quickstart.views import quick_start

urlpatterns = [
    path('hello/', quick_start),
]