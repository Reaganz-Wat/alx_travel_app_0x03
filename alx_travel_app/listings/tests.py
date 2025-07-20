from django.test import TestCase

# Create your tests here.
class MyTest(TestCase):
    def test_name(self):
        self.assertEquals("Watmon", "Watmon", "This is my name test")

    def test_age(self):
        self.assertEquals(24, 24, "This is watmons age")