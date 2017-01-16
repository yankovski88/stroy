# -*- coding: utf-8 -*-
from django.db import models

class IndexCl (models.Model): # создаем все что касается простой модели
    class Meta (): # обзавем наш класс
        db_table = 'index_cl'


    title_index = models.CharField (max_length=128, blank=True, verbose_name='Заголовок')
    text_index = models.TextField (blank=True, verbose_name='Текст')
    # pp_text = RichTextField(verbose_name='текст', blank=True, )
    date_index = models.DateTimeField(verbose_name='Дата', null='True' )

    def __unicode__(self):
        return self.title_index

