
from django.utils.translation import ugettext_lazy as _
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import exceptions as rest_exceptions

from apps.client_auth.models import Token


class TokenAuthentication(BaseAuthentication):
    """
    Simple token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:

        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """

    model = Token

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'token':
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise rest_exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise rest_exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise rest_exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.select_related('client').get(key=key)
        except self.model.DoesNotExist:
            raise rest_exceptions.AuthenticationFailed(_('Invalid token.'))

        if not token.client.is_active:
            raise rest_exceptions.AuthenticationFailed(_('client inactive or deleted.'))

        return (token.client, token)

    def authenticate_header(self, request):
        return 'Token'
