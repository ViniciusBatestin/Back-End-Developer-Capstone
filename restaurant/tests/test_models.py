from django.test import TestCase
from ..models import Menu
from ..serializers import MenuSerializer

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=5, inventory=100)
        self.assertEqual(str(item), "IceCream : 5")

class MenuViewTest(TestCase):
    def setUp(self):
        self.pizza = Menu.objects.create(title='pizza', price=12, inventory=10)
        self.pastel = Menu.objects.create(title='pastel', price=5, inventory=10)

    def test_getall(self):
        menus = Menu.objects.all()
        serialized_data = MenuSerializer(menus, many=True).data
        self.assertEqual(len(serialized_data), 2) # Check if 2 items were serialized
        self.assertEqual(serialized_data[0]['title'], "pizza") # Verify item
