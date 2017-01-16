# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from nrokdv.views import nrokdv

urlpatterns = patterns('',

url (r'^$', nrokdv),
                       )
