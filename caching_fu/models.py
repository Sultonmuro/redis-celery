from django.db import models

# Create your models here.


class Scheduler(models.Model):
    name = models.CharField(blank=False)