from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver
from .models import Article

@receiver(pre_save, sender=Article)
def generate_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
