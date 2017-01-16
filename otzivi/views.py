# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect # будет сообщать что форма отправлена успешно
from otzivi.forms import OtziviForm # импортировали наш класс с формс
from otzivi.forms import OtziviCl # имп


def otzivi_name (request):
    if request.method == 'POST': # отправим данные методом POST
        form = OtziviForm (request.POST) # создали форму для словаря


        if form.is_valid():
            print form.cleaned_data # все что правильно заполненое вывести
            form.save() # форму сохранить
        return HttpResponseRedirect ('/dobavit/redirect/') # пишем перевести на другую страницу все правильно

    else:
        form = OtziviForm() # иначе вернуть обратно форму
    return render(request, 'otziviform.html', {'form': form}) #



def otzivi_redirect (request):
    return render_to_response('redirect.html')



def otzivi_base (request):
    otzivi_base1 = OtziviCl.objects.all()
    return render_to_response('otzivi.html', {'otzivi_base2': otzivi_base1})