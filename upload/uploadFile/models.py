from django.db import models

class ProfilImage(models.Model):
    image = models.FileField(upload_to='upload/profile/%y/%m/%d')

    
    def __str__(self):
        return "{}".format(self.image)
