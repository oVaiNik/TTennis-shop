from statistics import quantiles
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from carts.models import Cart
from orders.models import Order, OrderItem
from goods.models import Products

from .models import User

User = get_user_model()

#unit-тест
class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username = "testuser",
            first_name = "test_first_name",
            last_name = "test_last_name",
            email="operation_test@gmail.com",
            password = "Operation_pass523",
            phone_number = "9141234567",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.first_name, "test_first_name")
        self.assertEqual(user.last_name, "test_last_name")
        self.assertEqual(user.email, "operation_test@gmail.com")
        self.assertTrue(user.check_password("Operation_pass523"))
        self.assertFalse(user.check_password("Operation_pass5wqr"))
        self.assertEqual(user.phone_number, "9141234567")
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        admin = User.objects.create_superuser(
            username = "admin",
            email = 'operation_ad@gmail.com',
            password = 'Operation_pass512',
        )
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)
        