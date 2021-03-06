# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Pin, Vote

def index(request):
    latest_pin_list = Pin.objects.order_by('-pub_date')[:5]
    context = {
        'latest_pin_list': latest_pin_list
    }
    
    template = loader.get_template('pins/index.html')
    return HttpResponse(template.render(context, request))

def create(request):
    if request.method == 'GET':
       latest_pin_list = Pin.objects.order_by('-pub_date')[:5]
       template = loader.get_template('pins/create.html')
       context = {
           'latest_pin_list': latest_pin_list,
       }
       return HttpResponse(template.render(context, request))
       
    elif request.method == 'POST':
       pin = Pin ()  
       pin.pin_name = request.POST.get('pin_name')
       pin.pin_room = request.POST.get('pin_room')
       pin.pin_description = request.POST.get('pin_description')
       pin.date = request.POST.get('date')
       pin.pin_type = request.POST.get('pin_type')
       pin.save()
       return HttpResponse(index(request))

def clear(request):
    Pin.objects.all().delete()
    return HttpResponse ('Cleared pins')

def test(request):
    test_pin = Pin ()
    test_pin.pin_name = 'test pin!'
    test_pin.pin_room = 105
    test_pin.pin_description = 'this is a test pin'
    test_pin.date = '2018-12-10 09:23:00'
    test_pin.save()
    return HttpResponse('Test pin')
    
def getAllRoomPins (request):
    numberOfPins = len(Pin.objects.filter(pin_room = request.GET.get('room')))
    return HttpResponse("Number of Pins: " + str(numberOfPins))



