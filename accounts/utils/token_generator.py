import six
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator




class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: AbstractBaseUser, timestamp: int) -> str:
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
        )
        

account_activation_token = AccountActivationTokenGenerator()