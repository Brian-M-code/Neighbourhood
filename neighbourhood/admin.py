from django.contrib import admin
from .models import Neighbourhood, Business, Category

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Category)