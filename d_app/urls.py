from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dockerize.views import AnimalViewSet

r = DefaultRouter()
r.register('animals', AnimalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls), ] + r.urls
