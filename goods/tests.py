from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from goods.models import Products, Categories

User = get_user_model()

class CatalogSearchTest(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(
            name='Обувь',
            slug='shoes'
        )
        
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00',
            content_type='image/jpeg'
        )
        
        self.converse = Products.objects.create(
            name='Кеды Converse Chuck Taylor',
            slug='converse-chuck-taylor',
            description='Классические кеды Converse с высоким верхом',
            price=2999,
            category=self.category,
            image=self.test_image
        )
        
        self.nike = Products.objects.create(
            name='Кроссовки Nike Air Force 1',
            slug='nike-air-force-1',
            description='Культовые кроссовки Nike с подошвой Air',
            price=5999,
            category=self.category,
            image=self.test_image
        )
        
        self.adidas = Products.objects.create(
            name='Кроссовки Adidas Superstar',
            slug='adidas-superstar',
            description='Легендарные кроссовки Adidas с ракушкой',
            price=4999,
            category=self.category,
            image=self.test_image
        )

    def test_search_ranking(self):
        response = self.client.get(reverse('goods:search'), {'q': 'кроссовки'})
        results = response.context['goods']
        
        found_products = {p.name for p in results}
        expected_products = {
            'Кроссовки Nike Air Force 1',
            'Кроссовки Adidas Superstar'
        }
        
        for expected in expected_products:
            self.assertIn(expected, found_products)
        
        self.assertNotIn('Кеды Converse Chuck Taylor', found_products)
        
        if len(results) > 1:
            self.assertTrue('кроссовки' in results[0].name.lower())

    def test_search_exact_match(self):
        response = self.client.get(reverse('goods:search'), {'q': 'Converse'})
        results = response.context['goods']
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, 'Кеды Converse Chuck Taylor')

    def test_search_partial_match(self):
        response = self.client.get(reverse('goods:search'), {'q': 'Nike'})
        results = response.context['goods']
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, 'Кроссовки Nike Air Force 1')

    def test_search_no_results(self):
        response = self.client.get(reverse('goods:search'), {'q': 'Puma'})
        results = response.context['goods']
        self.assertEqual(len(results), 0)