# -*- coding: utf-8 -*-
from django.db import models

class OtziviCl (models.Model): # создаем все что касается простой модели
    class Meta (): # обзавем наш класс
        db_table = 'otzivi_cl'


    title = models.CharField (max_length=128, blank=True, verbose_name='Заголовок')
    text_ckred = models.TextField (blank=True, verbose_name='Текст')


    def __unicode__(self):
        return self.title

