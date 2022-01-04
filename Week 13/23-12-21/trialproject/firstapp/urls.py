from django.contrib import admin
from django.urls import path
from firstapp import views

urlpattern = [
path('firstappFirstview/',views.views_one),
path('secondappSecondview/',views.views_two),
]