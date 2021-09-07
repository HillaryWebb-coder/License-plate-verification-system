from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, verbose_name=("Citizen"), on_delete=models.CASCADE)
    address = models.CharField(_("Address"), max_length=50)
    plate_number = models.CharField(_("Plate Number"), max_length=50)


class Log(models.Model):

    user_profile = models.ForeignKey(Profile, verbose_name=_("User Details"), on_delete=models.CASCADE, blank=True, null=True)
    plate_number = models.CharField(_("Plate Number"), max_length=500, blank=True)
    offence = models.CharField(_("Offence"), max_length=500, blank=True, null=True)
    image = models.ImageField(_('Image'), upload_to='images/')