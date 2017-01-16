# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from nrelectro.models import NrElectroClass
# проверка или удалятся файлы закинутые вручную на сервере


def nrelectro (request):
    nr1 = NrElectroClass.objects.all()
    return render_to_response('nrelectro.html', {'nr1': nr1})

# Create your views here.
