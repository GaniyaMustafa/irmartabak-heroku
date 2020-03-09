from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, editable=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self):
        self.slug = slugify(self.title)
        super().save()

        def __str__(self):
            return "{}. {}".format(self.id, self.title)
