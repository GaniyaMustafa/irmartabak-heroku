from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.ProfilImageView),
    path('result/', v.result),
]
