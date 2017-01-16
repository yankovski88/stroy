# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from santeh.views import nrsanteh

urlpatterns = patterns('',

url (r'^$', nrsanteh),
                       )
