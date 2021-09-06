from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .identification import IdentifyImage

from .models import Log

@receiver(post_save, sender=Log)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        image = instance.image.url
        plate_number = IdentifyImage(image).getNumber()
        instance.plate_number = plate_number
        instance.save()