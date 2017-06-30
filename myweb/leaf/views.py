# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_page(request):
    return HttpResponse("<p>叶子</p>")
