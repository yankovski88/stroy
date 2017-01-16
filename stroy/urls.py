# -*- coding: utf-8 -*-
"""stroy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
url(r'^admin/', include(admin.site.urls)),
url (r'^$', include ('index.urls')), # это главная страница
url (r'^nr/', include ('nr.urls')), # это наши работы
url (r'^nrelectro/', include ('nrelectro.urls')), # это нашиработы электро монтаж
url (r'^nrsanteh/', include ('santeh.urls')), # это нашиработы сантехнические работы
url (r'^nrokdv/', include ('nrokdv.urls')), # это нашиработы окна и двери


url (r'^nu/', include ('nu.urls')), # это наши услуги
url(r'^formsa/', include('form.urls', namespace='formsa')),  # форма под урок,
url (r'^otzivi/', include ('otzivi.urls')), # отзывы главная главная
url (r'^dobavit/', include ('otzivi.urls')), # отзывы редирект
url (r'^us/', include ('us.urls')), # о нас
url (r'^blog/', include ('blog.urls')), # блог

]
