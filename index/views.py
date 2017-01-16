# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from index.models import IndexCl

def index (request):
    index2 = IndexCl.objects.all()
    return render_to_response('index.html', {'index3': index2})