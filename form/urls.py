# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from form.views import post_list, post_new,post_detali, post_edit


urlpatterns = patterns('',
                       url(r'^$', post_list, name='post_list'),
                       url(r'^post/new/$', post_new, name='post_new'), # name='post_new по названию функции
                       url(r'^post/(?P<pk>[0-9]+)/$', post_detali, name='post_detali'),
                       url(r'^post/(?P<pk>[0-9]+)/edit/$', post_edit, name='post_edit'), # url для редакции
                       )
