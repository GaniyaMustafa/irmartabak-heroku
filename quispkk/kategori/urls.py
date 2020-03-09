from django.urls import path
from . import views as v

urlpatterns = [
    path('m/kategori/', v.kategori),
    path('m/produk/', v.produk),
    path('m/laporan/', v.laporan),
    path('m/', v.menu),
]
