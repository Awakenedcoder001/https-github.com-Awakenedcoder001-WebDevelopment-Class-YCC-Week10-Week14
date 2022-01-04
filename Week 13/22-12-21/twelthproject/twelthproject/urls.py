"""twelthproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jobsapp import views as v1
from sportsapp import views as v2
from touristapp import views as v3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.salt_is_bae),
    path('pornhub',v1.pornhub_company),
    path('youtube',v1.youtube_company),
    path('Wrestle',v2.WWE_Wrestler),
    path('Gamer',v2.Esports_Gamers),
    path('Dancer',v2.Dance_off),
    path('PlaceTphu',v3.Thimphu),
    path('PlacePro',v3.Paro),
]


