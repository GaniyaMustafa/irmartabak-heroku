from django.contrib import admin
from django.urls import path, include
from . import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index),
    path('', include('blog.urls')),
]
