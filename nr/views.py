# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from nr.models import NrClass
# проверка или удалятся файлы закинутые вручную на сервере
def nr (request):
    nr1 = NrClass.objects.all()
    return render_to_response('nr.html', {'nr1': nr1})




