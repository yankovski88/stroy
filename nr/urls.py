# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from nr.views import nr

urlpatterns = patterns('',
url (r'^$', nr),

                       )
