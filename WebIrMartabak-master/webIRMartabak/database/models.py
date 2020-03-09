from django.db import models
from django.utils.text import slugify

class martabak(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="static/img/upload/%y/%m/%d")
    price = models.IntegerField()
    variant = models.CharField(max_length=50, choices=[("Manis", "Manis"), ("Asin", "Asin")], default="Manis")
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.name)
        super(martabak, self).save()

    def __str__(self):
        return "{}".format(self.name)

class martabakhome(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img/upload/")
    price = models.IntegerField()    
    rating = models.IntegerField()    

    def __str__(self):
        return "{}".format(self.name)


