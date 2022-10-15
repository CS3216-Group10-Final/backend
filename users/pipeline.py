from .models import User

def link_account(user, details, strategy, *args, **kwargs):
    if user and details['player']:
        for name, value in details['player'].items():
            if value is not None and hasattr(user, name):
                setattr(user, name, value)