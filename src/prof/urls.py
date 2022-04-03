from django.contrib import admin
from django.urls import path
from .views import CompteList, CompteCreate

app_name = "prof"
urlpatterns = [
    path('create/', CompteCreate.as_view(), name='create'),
]
