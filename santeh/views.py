# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from santeh.models import NrSantehClass
# проверка или удалятся файлы закинутые вручную на сервере


def nrsanteh (request):
    nr1 = NrSantehClass.objects.all()
    return render_to_response('santeh.html', {'nr1': nr1})

# Create your views here.
