from django.test import TestCase
from .models import Product
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class ProductModelTest(TestCase):

    def test_create_product(self):
        product = Product.objects.create(
            name="Lamp",
            price=77.00,
            description="A small lamp"
        )

        self.assertEqual(product.name, "Lamp")
        self.assertEqual(product.price, 77.00)
        self.assertEqual(Product.objects.count(), 1)




