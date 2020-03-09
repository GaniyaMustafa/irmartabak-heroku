from . import views as v
from django.urls import path

urlpatterns = [
    path('about/', v.index),
    path('about/detail/', v.detail),
]