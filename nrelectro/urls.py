# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from nrelectro.views import nrelectro

urlpatterns = patterns('',

url (r'^$', nrelectro),
                       )
