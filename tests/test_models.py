from django.test import TestCase
from my_app1.models import Person, Car

class PersonTestCase (TestCase):
    def setUp(self):
        Person.objects.create(first_name="one",last_name="two", city="lviv")
        Person.objects.create(first_name="oneone",last_name="twotwo", city="odesa")


    def test_creation(self):
        person1=Person.objects.get(first_name="one")
        person2=Person.objects.get(first_name="oneone")
        self.assertEqual(person1.last_name,"two")
        self.assertEqual(person2.last_name,"twotwo")
        self.assertEqual(person1.city,"lviv")
        self.assertEqual(person2.city,"odesa")


class CarTestCase (TestCase):
    def setUp(self):
        Car.objects.create(year="2000",car_name="bmw")
        Car.objects.create(year="2010",car_name="vw")
    
    def test_creation(self):
        car1=Car.objects.get(year="2000")
        car2=Car.objects.get(year="2010")
        self.assertEqual(car1.car_name,"bmw")
        self.assertEqual(car2.car_name,"vw")
