from django.contrib import admin
from .models import martabak, martabakhome

class MartabakSlug(admin.ModelAdmin):
    readonly_fields = [
        'slug',
    ]

admin.site.register(martabak, MartabakSlug)
admin.site.register(martabakhome)
