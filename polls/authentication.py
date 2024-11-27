from tastypie.models import ApiKey
from tastypie.http import HttpUnauthorized
from tastypie.authentication import Authentication
from django.core.exceptions import ObjectDoesNotExist
from tastypie.compat import (
    get_user_model, get_username_field, compare_sanitized_tokens, InvalidTokenFormat, check_token_format
)
# Follow tastypie / still confuse between authorization and authentication syntax
# HTTP_AUTHORIZATION target specific username and api key
class CustomHTTPAuthentication(Authentication):
    def _unauthorized(self):
        return HttpUnauthorized()

    def is_authenticated(self, request, **kwargs):
        if not(request.META.get('HTTP_AUTHORIZATION')) or not(request.META.get('HTTP_USERNAME')):
            return self._unauthorized()
        
        username = request.META['HTTP_USERNAME']
        api_key = request.META['HTTP_AUTHORIZATION']
        key_auth_check = self.get_key(api_key,request)
        name_auth_check = self.get_name(username,request)
        return key_auth_check and name_auth_check
    
    def get_name(self, username, request):
            """
            Finding Api Key from UserProperties Model
            """
            username_field = get_username_field()
            User = get_user_model()
            try:
                lookup_kwargs = {username_field: username}
                user = User.objects.get(**lookup_kwargs)
            except ObjectDoesNotExist:
                return self._unauthorized()
            return True

    def get_key(self, api_key, request):
        """
        Finding Api Key from UserProperties Model
        """
        try:
            key = ApiKey.objects.get(key=api_key)
        except ObjectDoesNotExist:
            return self._unauthorized()
        return True