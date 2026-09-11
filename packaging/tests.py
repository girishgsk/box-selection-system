from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Box, Product


class BoxRecommendationAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Products
        cls.laptop = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2,
        )

        cls.keyboard = Product.objects.create(
            name="Keyboard",
            length=45,
            width=15,
            height=5,
            weight=1,
        )

        cls.heavy_product = Product.objects.create(
            name="Heavy Machine",
            length=20,
            width=20,
            height=20,
            weight=15,
        )

        cls.large_product = Product.objects.create(
            name="Large Product",
            length=100,
            width=100,
            height=100,
            weight=5,
        )

        # Boxes
        cls.small_box = Box.objects.create(
            name="Small Box",
            length=35,
            width=25,
            height=10,
            max_weight=5,
            cost=50,
        )

        cls.medium_box = Box.objects.create(
            name="Medium Box",
            length=50,
            width=35,
            height=20,
            max_weight=10,
            cost=80,
        )

        cls.large_box = Box.objects.create(
            name="Large Box",
            length=70,
            width=50,
            height=40,
            max_weight=20,
            cost=120,
        )

    def test_single_product_returns_smallest_suitable_box(self):
        response = self.client.post(
            "/api/recommend-box/",
            {
                "products": [
                    {
                        "product_id": self.laptop.id,
                        "quantity": 1,
                    }
                ],
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["recommended_box"]["name"],
            "Small Box",
        )

    def test_multiple_products_returns_suitable_box(self):
        response = self.client.post(
            "/api/recommend-box/",
            {
                "products": [
                    {
                        "product_id": self.laptop.id,
                        "quantity": 1,
                    },
                    {
                        "product_id": self.keyboard.id,
                        "quantity": 1,
                    },
                ],
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["recommended_box"]["name"],
            "Medium Box",
        )

    def test_quantity_is_respected(self):
        response = self.client.post(
            "/api/recommend-box/",
            {
                "products": [
                    {
                        "product_id": self.keyboard.id,
                        "quantity": 2,
                    }
                ],
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["recommended_box"]["name"],
            "Medium Box",
        )
    def test_product_rotation_is_allowed(self):
        # Product dimensions: 10 x 30 x 20
        # Box dimensions:     35 x 25 x 10
        # It only fits when rotated.
        rotated_product = Product.objects.create(
            name="Rotated Product",
            length=10,
            width=30,
            height=20,
            weight=1,
        )

        response = self.client.post(
            "/api/recommend-box/",
            {
                "products": [
                    {
                        "product_id": rotated_product.id,
                        "quantity": 1,
                    }
                ],
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["recommended_box"]["name"],
            "Small Box",
        )

    def test_weight_limit_is_respected(self):
        response = self.client.post(
            "/api/recommend-box/",
            {
                "products": [
                    {
                        "product_id": self.heavy_product.id,
                        "quantity": 1,
                    }
                ],
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["recommended_box"]["name"],
            "Large Box",
        )

    def test_no_suitable_box_returns_404(self):
        response = self.client.post(
            "/api/recommend-box/",
            {
                "products": [
                    {
                        "product_id": self.large_product.id,
                        "quantity": 1,
                    }
                ],
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_invalid_product_returns_400(self):
        response = self.client.post(
            "/api/recommend-box/",
            {
                "products": [
                    {
                        "product_id": 99999,
                        "quantity": 1,
                    }
                ],
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

        self.assertIn(
            "does not exist",
            response.data["error"],
        )

    def test_invalid_quantity_returns_400(self):
        response = self.client.post(
            "/api/recommend-box/",
            {
                "products": [
                    {
                        "product_id": self.laptop.id,
                        "quantity": 0,
                    }
                ],
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_empty_products_returns_400(self):
        response = self.client.post(
            "/api/recommend-box/",
            {
                "products": [],
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_missing_products_returns_400(self):
        response = self.client.post(
            "/api/recommend-box/",
            {},
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )