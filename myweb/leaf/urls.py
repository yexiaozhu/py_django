#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

from django.conf.urls import include, url
import views

urlpatterns = [ # 1.11.2 去掉patteerns
    url(r'^$', views.first_page, name='first_page'),
    url(r'^staff', views.staff, name='staff'),
    url(r'^templay', views.templay, name='templay'),
    #url(r'^$', 包名.first_page, name='first_page'),
]