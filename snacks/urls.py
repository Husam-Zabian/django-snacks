from django.contrib import admin
from django.urls import path
from .views import HomePageView,AboutPageView


urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('aboutus',AboutPageView.as_view(), name='about')
]