from django.db import models


class Matter(models.Model):
    logoid = models.CharField(max_length=7)
    logohead = models.CharField(max_length=100)
    logocust = models.CharField(max_length=100)
    whom = models.CharField(max_length=100)
    logodate = models.DateTimeField()
    logopack = models.CharField(max_length=100,default='')
    logocontent = models.TextField(default='')
