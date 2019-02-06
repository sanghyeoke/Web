from django.db import models

# Create your models here.
class MainProfile(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    age = models.IntegerField()
    area = models.CharField(max_length=15)
    favorite = models.CharField(max_length=300)
    hello = models.CharField(max_length=1000)

    def __str__(self):
        return self.name