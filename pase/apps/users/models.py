from django.contrib.auth.models import User, UserManager
from django.utils.translation import ugettext_lazy as _

class BaseUserManager(UserManager):

    def create_user(self, username, email=None, password=None, **extra_fields):
        return super(BaseUserManager, self).create_user(username, email, password, **extra_fields)
        # write additional code


class BaseUser(User):

    objects = BaseUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return self.username
