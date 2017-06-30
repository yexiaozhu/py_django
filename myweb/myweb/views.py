#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

from django.http import HttpResponse

def first_page(request):
    return HttpResponse("<p>hello mayday</p>")