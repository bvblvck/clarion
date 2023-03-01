# -*- encoding: utf-8 -*-


from django.contrib import admin
from .models import deposit, variables

# Register your models here.
admin.site.register(deposit)
admin.site.register(variables)