from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("hotel", views.hotel, name='hotel'),
    path("ticket", views.ticket, name='ticket'),
    path("holidays", views.holidays, name='holidays'),
    path("home", views.index, name='home'),
    path("places", views.places, name='places')
]
