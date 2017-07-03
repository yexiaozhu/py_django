# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from models import Character

def first_page(request):
    return HttpResponse("<p>叶子</p>")

def staff(request):
    staff_list = Character.objects.all()
    # staff_str = map(str, staff_list)
    # context = {'label': ' '.join(staff_str)}
    return render(request, 'templay.html', {'staffs': staff_list})

def templay(request):
    context = {}
    context['label'] = 'Hello World! This is from myweb'
    return render(request, 'templay.html', context)