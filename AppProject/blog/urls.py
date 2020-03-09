from . import views as v
from django.urls import path

urlpatterns = [
    path('blog/', v.index),
    path('blog/detail/', v.detail),
]