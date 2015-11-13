import os
import binascii
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ClientManager(models.Manager):
    pass


class Client(models.Model):
    """
    Client model to access site authorized information
    """
    name = models.CharField(max_length=100, verbose_name=_("Client Name"))
    api_key = models.CharField(max_length=40, unique=True, blank=True, db_index=True)
    is_active = models.BooleanField(default=True)

    objects = ClientManager()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = self.generate_key()
        return super(Client, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')
