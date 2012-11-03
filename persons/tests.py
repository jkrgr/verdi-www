"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

"""

from django.test import TestCase
from persons.models import User


class PersonTest(TestCase):
    def setUp(self):
        """ Create some data to test against
        """
        p = User()
        p.first_name = "Joachim"
        p.last_name = "Kruger"
        p.email = "jk@redpai.no"
        p.username = p.email
        p.position = 'Analyst'
        p.save()


    def test_user(self):
        pers = User.objects.all()[0]
        self.assertEqual(pers.first_name, 'Joachim')
        self.assertEqual(pers.username, 'jk@redpai.no')

