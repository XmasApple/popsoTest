from django.db import models


# Create your models here.
class ParsedData(models.Model):
    text = models.CharField(max_length=4096)
    tag = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    photo_path = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.text
