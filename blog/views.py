# -*- coding: utf-8 -*-
from blog.models import BlogClass
from django.shortcuts import render_to_response

# проверка или удалятся файлы закинутые вручную на сервере
def blog (request):
    blog1 = BlogClass.objects.all()
    return render_to_response('blog.html', {'blog1': blog1})

# Create your views here.
