# -*- coding: utf-8 -*-
from django.db import models

# запоминать пользователя
# автосохранение даты
from django.utils import timezone


class Post (models.Model):
    class Meta ():
        db_table = 'form_app'


    author = models.ForeignKey('auth.User')   #ForeignKey это связь одного ко многим(1 пользователь, 5 статей)
    #вот тогда добовляем ForeignKey один ко многим, одна статья моного камментариев
    # auth.User' это модель пользователя, в админке пользователя можно добовлять
    post_title = models.CharField (max_length=200)
    post_text = models.TextField (blank=False)
    post_created_date = models.DateTimeField (default= timezone.now)
    post_publiched_date = models.DateTimeField (blank=True, null = True) # дата побликации

    def publich (self):
        self.post_publiched_date = timezone.now ()
        self.save () # оператор сохранить

    def __unicode__(self): # чтоб по заголовку выводилось
        return self.post_title
