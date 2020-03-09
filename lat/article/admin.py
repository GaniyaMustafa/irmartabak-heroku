from django.contrib import admin
from . import models

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = [
        'create_at',
        'update_at',
        'slug',
    ]
admin.site.register(models.Article, ArticleAdmin)