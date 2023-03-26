from django.contrib import admin
from django.urls import path

from core import views
urlpatterns = [
    path("", views.index, name="core"),
    path("btech", views.btech, name="btech"),
    path("mtech", views.mtech, name="mtech"),
    path("phd", views.phd, name="phd"),
    path("home",views.home,name="home"),
    path("about",views.about,name="about"),
    path("404",views.nn,name="404")
]
