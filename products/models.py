from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('Price'))
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Create date'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Update date'))

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])

class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(active=True)

class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE, related_name='comments', verbose_name=_('Comment author'))
    body = models.TextField(verbose_name=_('Comment Text'), max_length=200)
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('What is your score?'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Product'))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Create date'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Update date'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))

    # manager
    objects = models.Manager()
    active_comment_manager = ActiveCommentManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
