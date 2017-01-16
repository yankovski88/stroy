# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from us.models import UsClass

def us2 (request):
    us = UsClass.objects.all()
    return render_to_response('us.html', {'us1': us})

# Create your views here.
