from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title