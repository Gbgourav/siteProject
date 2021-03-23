from django.shortcuts import render, HttpResponse
from django.template import context
from home.models import Contact, Hotel, Ticket
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')

def hotel(request):
    if request.method== 'POST':
        name = request.POST.get('name')
        destination = request.POST.get('destination')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        hotel = Hotel(name=name, destination=destination, email=email, phone=phone, desc=desc, date= datetime.today())
        hotel.save()
        messages.success(request, 'Your hotel booking request has submitted our team will contact you soon.')

    return render(request, 'hotel.html') 

def ticket(request):
    if request.method== 'POST':
        name = request.POST.get('name')
        destination = request.POST.get('destination')
        city = request.POST.get('city')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        ticket = Ticket(name=name, destination=destination, city=city, email=email, phone=phone, desc=desc, date= datetime.today())
        ticket.save()
        messages.success(request, 'Your ticket request has been submitted our team will contact you soon.')

    return render(request, 'ticket.html')  

def holidays(request):
    return render(request, 'holidays.html')  


def home(request):
    return render(request, 'index.html')    
            

def contact(request):
    if request.method== 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent.')

    return render(request, 'contact.html')


def places(request):
    return render(request, 'places.html')      
  
