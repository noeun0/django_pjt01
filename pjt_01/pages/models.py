from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    path = models.CharField(max_length=100)

    def __str__(self):
        return self.title