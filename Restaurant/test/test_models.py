from django.test import TestCase
from Restaurant.models import Menu
from decimal import Decimal
class MenuItemTest(TestCase):
    def setUp(self):
        menu1 = Menu.objects.create(title='Idly',price=Decimal('10.00'))
    def test_get_item(self):
        item = Menu.objects.get(title='Idly',price=Decimal('10.00'))
        self.assertEqual(str(item),"Idly : 10.00")