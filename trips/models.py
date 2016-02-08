from __future__ import unicode_literals
from django.db import models

""" Trip object to store one Trip """
class Trip(models.Model):
    """ Name of the Trip """
    name = models.CharField(max_length=55)
    """ Start date of the Trip """ 
    start_date = models.DateField()
    """ End date of the Trip """
    finish_date = models.DateField()
    
    """ Returns this Trip's name """
    def getTripName(self):
        return self.name
        
    """ Returns this Trip's start_date """
    def getTripStartDate(self):
        return self.start_date

    """ Returns this Trip's finish_date """
    def getTripFinishDate(self):
        return self.finish_date