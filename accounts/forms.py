from django import forms
from django.core import validators




class RegisterForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,  
        label='نام کاربری حداقل تا 3 کاراکتر',  
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'class': 'input is-info is-medium bg-light',
            'placeholder': 'نام کاربری خود را وارد کنید',
            'id': 'username',
        },),
    )
    
    first_name = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,  
        label='نام بین 3 تا 64 کاراکتر',  
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'class': 'input is-info is-medium bg-light',
            'placeholder': 'نام خود را وارد کنید',
            'id': 'fname',
        },),
    )
    
    last_name = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,  
        label='نام خانوادگی بین 3 تا 64 کاراکتر',  
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'class': 'input is-info is-medium bg-light',
            'placeholder': 'نام خانوادگی خود را وارد کنید',
            'id': 'lname',
        },),
    )
    
    email = forms.EmailField(
        max_length=150,
        required=True,
        label='ایمیل حداکثر تا 150 کاراکتر',
        validators=[
            validators.EmailValidator(),
        ],
        widget=forms.EmailInput(attrs={
            'class': 'input is-info is-medium bg-light',
            'placeholder': 'لطفا ایمیل خود را وارد کنید',   
            'id': 'email',
        },),
    )
    
    password = forms.CharField(
        min_length=6,
        max_length=64,
        required=True,
        label='رمز ورود حداقل بین 6 تا 64 کاراکتر (ترکیب حروف و اعداد)',
        validators=[
            validators.MinLengthValidator(limit_value=6),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.PasswordInput(attrs={
            'class': 'input is-info is-medium bg-light',
            'placeholder': 'رمز خود را وارد کنید',
            'id': 'pass',
        },),
    )
    
    con_password = forms.CharField(
        min_length=6,
        max_length=64,
        required=True,
        label='تایید مجدد رمز ورود',
        validators=[
            validators.MinLengthValidator(limit_value=6),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.PasswordInput(attrs={
            'class': 'input is-info is-medium bg-light',
            'placeholder': 'رمز خود را دوباره وارد کنید',
            'id': 'conpass',
        },),
    )
    
    



class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,
        label='نام کاربری حداقل تا 3 کاراکتر',    
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'class': 'input is-info is-medium bg-light',
            'placeholder': 'نام کاربری خود را وارد کنید',
            'id': 'username',
        },),
    )
    
    password = forms.CharField(
        min_length=6,
        max_length=64,
        required=True,
        label='رمز ورود حداقل بین 6 تا 64 کاراکتر (ترکیب حروف و اعداد)',
        validators=[
            validators.MinLengthValidator(limit_value=6),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.PasswordInput(attrs={
            'class': 'input is-info is-medium bg-light',
            'placeholder': 'رمز خود را وارد کنید',
            'id': 'pass'
        },),
    )
    




class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(
        min_length=11,
        max_length=11,
        required=True,
        label='',
        validators=[
            validators.MinLengthValidator(limit_value=11),
            validators.MaxLengthValidator(limit_value=11),
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-light',
            'placeholder': 'شماره تلفن خود را وارد کنید',
            'id': 'phnumber'
        },),
    )
    
    




class ResetPasswordForm(forms.Form):
    email = forms.EmailField(
        max_length=150,
        required=True,
        label='ایمیل حداکثر تا 150 کاراکتر',
        validators=[
            validators.EmailValidator(),
        ],
        widget=forms.EmailInput(attrs={
            'class': 'input is-info is-medium bg-light',
            'placeholder': 'لطفا ایمیل خود را وارد کنید',   
            'id': 'email',
        },),
    )






class ResetPasswordConfirmForm(forms.Form):
    new_password = forms.CharField(
        min_length=6,
        max_length=64,
        required=True,
        label='رمز ورود جدید حداقل بین 6 تا 64 کاراکتر (ترکیب حروف و اعداد)',
        validators=[
            validators.MinLengthValidator(limit_value=6),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.PasswordInput(attrs={
            'class': 'input is-info is-medium bg-light',
            'placeholder': 'رمز جدید خود را وارد کنید',
            'id': 'pass',
        },),
    )
    
    con_new_password = forms.CharField(
        min_length=6,
        max_length=64,
        required=True,
        label='تایید مجدد رمز ورود جدید',
        validators=[
            validators.MinLengthValidator(limit_value=6),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.PasswordInput(attrs={
            'class': 'input is-info is-medium bg-light',
            'placeholder': 'رمز جدید خود را دوباره وارد کنید',
            'id': 'conpass',
        },),
    )