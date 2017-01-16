# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from nu.views import nu

urlpatterns = patterns('',
                       url (r'^$', nu),
                       )
