from django.db import models


class Set(models.Model):
    file = models.FileField (upload_to= 'files/wav')

class Vid(models.Model):
    file = models.FileField(upload_to = 'files/mp4')



# Create your models here.
