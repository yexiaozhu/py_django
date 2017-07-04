# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import Character, Contact, Tag
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline] # inline
    list_display = ('name', 'age', 'email') # list
    search_fields = ('name',)
    fieldsets = (
        ['Main',{
            'fields':('name', 'email'),
        }],
        ['Advance',{
            'classes': ('collapse',), #css
            'fields': ('age',),
        }]
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Character])