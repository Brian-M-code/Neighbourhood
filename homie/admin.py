# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Neighbourhood, Business, Post

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Post)
