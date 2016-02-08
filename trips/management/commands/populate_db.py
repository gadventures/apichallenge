from django.core.management.base import BaseCommand
from trips.models import Trip
from datetime import datetime, timedelta
import random

class Command(BaseCommand):

     """ Script to populate database with 100 randomized Trip objects """
     def handle(self, *args, **options):
        
        locations = ["London", "Toronto", "Paris", "New York", "Auckland", 
                    "Stockholm", "Dresden", "Shangai", "Dublin", "Moscow",
                    "Hong Kong", "Singapore", "Victoria", "Quebec", "Madrid"];
        tid = len(Trip.objects.all())
        
        for i in range(1, 101):
            
            year = random.choice(range(2016, 2018))
            month = random.choice(range(1, 13))
            day = random.choice(range(1, 29))
            
            start_date = datetime(year, month, day)
            end_date = start_date + timedelta(weeks=1)
            
            t = Trip(name=locations[random.choice(range(0, 15))], 
                                    start_date=start_date, 
                                    finish_date=end_date);
            t.save();
            