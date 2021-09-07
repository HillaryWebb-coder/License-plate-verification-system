from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .identification import IdentifyImage
import telegram_send
from .models import Log
# from django.contrib.sites.models import Site

@receiver(post_save, sender=Log)
def send_telegram_message(sender, instance, created, **kwargs):
    if created:
        image = instance.image.url
        # domain = Sites.object.get_current().domain
        image_url = 'http://127.0.0.1:8000' + image
        plate_number = IdentifyImage(image_url).getnumber()

        message = "Traffic Rule Violated!!!\nPLATE NUMBER: " + plate_number

        telegram_send.send(messages=[message], parse_mode='text')
        instance.plate_number = plate_number
        instance.save()