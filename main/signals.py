# signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import *



@receiver(post_save, sender=Product)
def product_saved(sender, instance, created, **kwargs) -> None :
    cache.delete('products')

@receiver(post_delete, sender=Product)
def product_deleted(sender, instance, **kwargs) -> None :
    cache.delete('products')

@receiver(post_save, sender=Category)
def product_saved(sender, instance, created, **kwargs) -> None :
    cache.delete('categories')

@receiver(post_delete, sender=Section)
def product_deleted(sender, instance, **kwargs) -> None :
    cache.delete('categories')

@receiver(post_save, sender=Section)
def product_saved(sender, instance, created, **kwargs) -> None :
    cache.delete('sections')

@receiver(post_delete, sender=Product)
def product_deleted(sender, instance, **kwargs) -> None :
    cache.delete('sections')