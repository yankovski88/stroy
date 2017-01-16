# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from nu.models import NuClass
# проверка или удалятся файлы закинутые вручную на сервере
def nu (request):
    nu1 = NuClass.objects.all()
    return render_to_response('nu.html', {'nu1': nu1})

# Create your views here.
