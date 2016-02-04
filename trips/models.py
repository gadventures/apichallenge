from __future__ import unicode_literals

from django.db import models

class Trip(models.Model):
    """
    The main Trip Model; added a few more attibutes! 
    """
    name = models.CharField(max_length=55)
    start_date = models.DateField()
    finish_date = models.DateField()
    tour_capacity = models.IntegerField()
    package_price = models.IntegerField()
    package_location = models.CharField(max_length=55)
