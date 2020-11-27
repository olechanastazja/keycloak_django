from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from rest_framework.exceptions import AuthenticationFailed


def get_user_by_keycloak_id(request, id_token):
    User = get_user_model()
    try:
        user = User.objects.get(email=id_token.get('email'))
    except User.DoesNotExist:
        msg = _('Invalid Authorization header. User not found.')
        raise AuthenticationFailed(msg)
    return user
