from django.test import TestCase
from .models import Pet

# Create your tests here.
class PetTest(TestCase):
    def test_string(self):
        type=Pet(petName="Dogs")
        self.assertEqual(str(type), type.petName)

    def test_table(self):
        self.assertEqual(str(Pet._meta.db_table), 'pet')