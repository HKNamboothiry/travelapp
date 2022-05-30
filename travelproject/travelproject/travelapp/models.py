from django.db import models

# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='image')
    desc=models.TextField()

    def __str__(self):
        return self.name

class TeamMembers(models.Model):
    name=models.CharField(max_length=250)
    member_photo=models.ImageField(upload_to='image')
    about=models.TextField()

    def __str__(self):
        return self.name