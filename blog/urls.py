# -*- coding: utf-8 -*-
from blog.views import blog
from django.conf.urls import url, patterns


urlpatterns = patterns('',
                       url (r'^$', blog),
                       )
