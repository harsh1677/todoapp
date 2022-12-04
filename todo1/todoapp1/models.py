from django.db import models

# Create your models here.
class todotable(models.Model):
    content = models.CharField(max_length=400, null=False)
    type = models.CharField(max_length=200, null=True, blank=True)