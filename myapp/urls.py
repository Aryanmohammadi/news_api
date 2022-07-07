from django.contrib import admin
from django.urls import path, include
from .views import news_view

urlpatterns = [
    path('',news_view),
]
