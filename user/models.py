from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class single(models.Model):
    name = models.CharField(max_length=100)
    template = CloudinaryField('image')
    video = CloudinaryField('videos')
    description = models.CharField(max_length=1000)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class group(models.Model):
    title = models.CharField(max_length=100)
    singles = models.ManyToManyField(single)
    img = CloudinaryField('image')
    cat = models.CharField(max_length=100)
    star = models.IntegerField(default=0)

    def __str__(self):
        return self.title


