from django.db import models


# Create your models here.
class File(models.Model):
    file = models.FileField(null=True, blank=True)

    class Meta:
        ordering = ('-id',)
