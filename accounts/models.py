from django.db import models
from django.core import validators
from django.contrib.auth.models import User





class UserPhoneNumber(models.Model):
    
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name='کاربر')
    phone_number = models.CharField(max_length=11, validators=[validators.MinLengthValidator(limit_value=11), validators.MaxLengthValidator(limit_value=11),], blank=True, null=True, unique=True, verbose_name='شماره تلفن')
    
    def __str__(self) -> str:
        super().__str__()
        return str(self.user)
    
    class Meta:
        verbose_name = 'شماره تلفن کاربر'
        verbose_name_plural = 'شماره تلفن کاربران'