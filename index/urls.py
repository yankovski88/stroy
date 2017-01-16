# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from index.views import index

urlpatterns = patterns('',
                       url (r'^$', index),
                       )
