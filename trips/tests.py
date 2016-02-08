from django.test import TestCase
from datetime import datetime, date
from models import Trip

# Create your tests here.
class TripTestCase(TestCase):
    def setUp(self):
        Trip.objects.create(name="London", 
                            start_date=date(2017, 5, 24), 
                            finish_date=date(2017, 9, 24))
        Trip.objects.create(name="Moscow", 
                            start_date=date(2017, 5, 24), 
                            finish_date=date(2017, 6, 24))
        
    def test_getTripName(self):
        trip = Trip.objects.get(name="London")
        self.assertEqual(trip.getTripName(), "London")
        
    def test_getTriStartDate(self):
        trip = Trip.objects.get(name="London")
        self.assertEqual(trip.getTripStartDate(), date(2017, 5, 24))
        
    def test_getTripFinishDate(self):
        trip = Trip.objects.get(name="London")
        self.assertEqual(trip.getTripFinishDate(), date(2017, 9, 24))