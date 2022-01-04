from django.contrib import admin
from django.urls.import path
from secondapp import views

urlpatterns=[
	path('secondappviewone/',views.view_one),
	path('secondappviewtwo/',views.view_two),
]