# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from nrokdv.models import NrOkdvClass
# проверка или удалятся файлы закинутые вручную на сервере


def nrokdv (request):
    nr1 = NrOkdvClass.objects.all()
    return render_to_response('santeh.html', {'nr1': nr1})

# Create your views here.
