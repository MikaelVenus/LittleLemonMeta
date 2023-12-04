from django.test import TestCase
from .models import Menu
# Create your tests here.
class MeniItemTestSuccess(TestCase):
     def test_get_item(self):
          item = Menu.objects.create(title="IceCream", price=70, inventory = 10)
          itemstr = item.get_item()
          self.assertEqual(itemstr, "IceCream : 70")

class MeniItemTestFail(TestCase):
     def test_get_item(self):
          item = Menu.objects.create(title="IceCream", price=80, inventory = 10)
          itemstr = item.get_item()
          self.assertEqual(itemstr, "IceCream : 70")
