from django.db import models

# Create your models here.

class MyModelName(models.Model):
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')

    class Meta:
        ordering = ['-my_field_name']

    def get_absolute_url(self):
        return reversed('model-detail-view',)