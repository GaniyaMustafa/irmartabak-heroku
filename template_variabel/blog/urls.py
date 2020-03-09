from django.urls import path
from django.urls import include
from . import views as v

urlpatterns = [
    path('blog/', v.index),
]