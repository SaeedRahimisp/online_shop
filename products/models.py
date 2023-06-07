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

class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(active=True)

class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect'),
    ]
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name='Comment Text', max_length=200)
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name='What is your score?')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # manager
    objects = models.Manager()
    active_comment_manager = ActiveCommentManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
