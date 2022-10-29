from django.shortcuts import redirect
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTStatelessUserAuthentication
from social_core.pipeline.partial import partial

def link_account(user, details, strategy, request, *args, **kwargs):
    id = strategy.session_get('user', None)
    jwt_object = JWTAuthentication()
    validated_token = jwt_object.get_validated_token(raw_token=id)
    user = jwt_object.get_user(validated_token=validated_token)

    if user and details['player']:
        for name, value in details['player'].items():
            if value is not None and hasattr(user, name):
                setattr(user, name, value)
                user.save()

@partial
def load_user(user, details, strategy, request, *args, **kwargs):
    user = strategy.session_get('usr', None)
    print('t2')
    print(user)
    if not user:
        return redirect("users.views.get_user")
    
    #set user

def debug(user, details, strategy, request, *args, **kwargs):
    print("test")
    request = strategy.request
    print(request.user)
