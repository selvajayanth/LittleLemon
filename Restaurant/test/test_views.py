from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from Restaurant.models import Menu
from decimal import Decimal
from django.contrib.auth.models import User
class MenuItemTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.menu1 = Menu.objects.create(title="Burger", price=Decimal(120))
        self.menu2 = Menu.objects.create(title="Pizza", price=Decimal(300))
    def test_get_all_items(self):
        response = self.client.get(reverse('menu-list-create'))#here data returned or fetched from test_db or original db?
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),2)# here data is property of response built in by APICLIENT?
    def test_create_items(self):
        url = reverse('menu-list-create')
        data = {'title':'Idly','price':Decimal(20)}
        item = self.client.post(url,data)
        self.assertEqual(item.status_code,status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(),3)#here Menu is representing original table or test_db? because it was imported the orignal Menu model
    def test_update_data(self):
        url = reverse('menu-update-delete',args=[self.menu1.id])
        data = {'title':'Dosa','price':210}
        res = self.client.put(url,data)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.menu1.refresh_from_db()
        self.assertEqual(self.menu1.title,'Dosa')
    def test_delte_item(self):
        url = reverse('menu-update-delete',args=[self.menu1.id])
        res = self.client.delete(url)
        self.assertEqual(res.status_code,status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(),1)