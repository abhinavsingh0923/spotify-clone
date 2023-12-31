from django.db import models

# Create your models here.

class Song(models.Model):
    name=models.CharField(max_length=50)
    artist=models.CharField(max_length=50)
    audio=models.FileField(upload_to='songs/', null=False,blank=False,max_length=200)

    def __str__(self) -> str:
        return self.name