from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Project(models.Model):
    titles = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portafolio/image/")
    url = URLField(blank=True)
    imageProject = models.ImageField(upload_to= 'portafolio_images/')
    contentProject = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    