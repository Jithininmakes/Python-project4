from django.db import models

# Create your models here.

class jithin (models.Model):
    name=models.CharField (max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField ()

    def __str__(self):
        return self.name

class inmakes (models.Model):
    nm=models.CharField (max_length=250)
    ig=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.nm
