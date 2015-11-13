import binascii
import os

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.client.models import Client


@python_2_unicode_compatible
class Token(models.Model):
    """
    The default authorization token model for clients.
    """
    key = models.CharField(max_length=40, primary_key=True)
    client = models.OneToOneField(Client, related_name="client_auth_token", verbose_name=_("Client Auth Token"))
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key

