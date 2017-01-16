# -*- coding: utf-8 -*-

from django.conf.urls import  url, patterns
from otzivi.views import  otzivi_name, otzivi_redirect, otzivi_base

urlpatterns = patterns('',
    url(r'^$', otzivi_base),
    url(r'^dobavit/$', otzivi_name),
    url(r'^redirect/$', otzivi_redirect),
                       )
