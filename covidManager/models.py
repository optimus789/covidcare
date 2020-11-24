from django.db import models


# Create your models here.


class Covidiot(models.Model):
    mob = models.CharField(max_length=100)
    fever = models.IntegerField()
    cough = models.IntegerField(default=1)
    breathlessness = models.IntegerField(default=1)
    smell = models.BooleanField(default=False)
    appetite =  models.BooleanField(default=False)
    tired = models.BooleanField(default=False)
    throat = models.BooleanField(default=False)
    bodypain = models.BooleanField(default=False)
    invisit = models.BooleanField(default=False)
    pubvisit = models.BooleanField(default=False)
    hivisit = models.BooleanField(default=False)
    xray = models.BooleanField(default=False)
    ctscan = models.BooleanField(default=False)
    pending_in = models.CharField(max_length=4000,null=True, blank=True)
    pending_out = models.CharField(max_length=4000,null=True, blank=True)
    friends = models.CharField(max_length=4000,null=True, blank=True)
    iv = models.CharField(max_length=200,null=True, blank=True)
    lat = models.CharField(max_length=2000,null=True,blank=True)
    lon = models.CharField(max_length=2000,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
