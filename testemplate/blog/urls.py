from django.urls import path
from . import views as v

urlpatterns = [
    path('blog/', v.index),
    path('blog/detail/', v.detail)
]
