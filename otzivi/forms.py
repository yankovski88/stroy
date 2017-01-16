# -*- coding: utf-8 -*-
from django.forms import ModelForm # импортировали нашу форму
from otzivi.models import OtziviCl # импортируем наш класс с моделей

class OtziviForm (ModelForm): # ну и создаем наш класс с добовление Form  и вставляем нашу форму
    class Meta:
        model = OtziviCl # cтандартная запись к модели
        fields = ['title', 'text_ckred'] # добавили наши поля с моделей