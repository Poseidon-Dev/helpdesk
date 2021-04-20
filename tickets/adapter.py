from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.forms import ValidationError

class CustomAccountAdapter(DefaultAccountAdapter):
    
    def clean_email(self, email):
        if not email.split('@')[1].lower() in settings.ACCOUNT_DOMAIN_WHITELIST:
            message = 'Your email is not within the list of accepted domains. If you believe this is a mistake, please try again or contact the system adminstrator'
            raise ValidationError(message)
        return email
