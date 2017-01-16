# -*- coding: utf-8 -*-

from django.conf.urls import  url, patterns
from us.views import  us2

urlpatterns = patterns('',
    url(r'^$', us2),
                       )