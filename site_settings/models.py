from django.db import models
from colorfield.fields import ColorField




class MainSiteSettings(models.Model):
    website_title = models.CharField(max_length=64, blank=True, null=True, verbose_name='عنوان وبسایت')
    website_header = models.CharField(max_length=64, blank=True, null=True, verbose_name='سرتیتر وبسایت')
    
    def __str__(self) -> str:
        super().__str__()
        return 'تنظیمات'
    
    class Meta:
        verbose_name = 'تنظیمات وبسایت'
        verbose_name_plural = 'تنظیمات وبسایت'
        
    




class SignUpSettings(models.Model):
    THEMES: list[tuple[str, str]] = [
        ('btn btn-success', '🟢 سبز'),
        ('btn btn-link', '🟦 آبی روشن'),
        ('btn btn-primary', '🔵 آبی تیره'),
        ('btn btn-warning', '🟡 زرد'),
        ('btn btn-danger', '🔴 قرمز'),
    ]
    
    page_title = models.CharField(max_length=64, blank=True, null=True, verbose_name='عنوان صفحهه')
    page_header = models.CharField(max_length=64, blank=True, null=True, verbose_name='سرتیتر صفحهه')
    page_username_input_hint = models.CharField(max_length=64, blank=True, null=True, verbose_name='نوشته ورودی نام کاربری')
    page_username_input_placeholder = models.CharField(max_length=128, blank=True, null=True, verbose_name='نوشته موقت ورودی نام کاربری')
    page_fname_input_hint = models.CharField(max_length=64, blank=True, null=True, verbose_name='نوشته ورودی نام')
    page_fname_input_placeholder = models.CharField(max_length=128, blank=True, null=True, verbose_name='نوشته موقت ورودی نام')
    page_lname_input_hint = models.CharField(max_length=64, blank=True, null=True, verbose_name='نوشته ورودی نام خانوادگی')
    page_lname_input_placeholder = models.CharField(max_length=128, blank=True, null=True, verbose_name='نوشته موقت ورودی نام خانوادگی')
    page_email_input_hint = models.CharField(max_length=64, blank=True, null=True, verbose_name='نوشته ورودی ایمیل')
    page_email_input_placeholder = models.CharField(max_length=128, blank=True, null=True, verbose_name='نوشته موقت ورودی ایمیل')
    page_password_input_hint = models.CharField(max_length=64, blank=True, null=True, verbose_name='نوشته ورودی رمز ورود')
    page_password_input_placeholder = models.CharField(max_length=128, blank=True, null=True, verbose_name='نوشته موقت ورودی رمز ورود')
    page_confirm_password_input_hint = models.CharField(max_length=64, blank=True, null=True, verbose_name='نوشته ورودی تایید رمز ورود')
    page_confirm_password_input_placeholder = models.CharField(max_length=128, blank=True, null=True, verbose_name='نوشته موقت ورودی تایید رمز ورود')
    page_button_text = models.CharField(max_length=32, blank=True, null=True, verbose_name='نوشته دکمه')
    page_button_color = models.CharField(max_length= 150, default='🟦 آبی روشن', choices=THEMES, verbose_name='رنگبندی دکمه')
    
    def __str__(self) -> str:
        super().__str__()
        return self.page_title
    
    class Meta:
        verbose_name = 'تنظیمات صفحه ورود به حساب کاربری'
        verbose_name_plural = 'تنظیمات صفحه ورود به حساب کاربری'