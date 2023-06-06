from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])

class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect'),
    ]
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=200)
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
