from django.contrib import admin
from django.urls import path, include
from . import views as v
from about import views as av

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index),
    path('', include('blog.urls')),
    path('', include('about.urls')),
]
