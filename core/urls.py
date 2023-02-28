# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include  # add this

admin.site.site_title = 'Clarion- Admin panel'
admin.site.site_header = 'Clarion-Trades'
admin.site.index_title = 'Administration'
urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),  # UI Kits Html files   

]
