from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title="Pizza", price=10, inventory=5)
        self.menu2 = Menu.objects.create(title="Burger", price=5, inventory=10)

    def test_getall(self):
        response = self.client.get('/api/menu-items/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)

