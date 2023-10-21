from django.contrib import admin

from .models import UserPhoneNumber


class PhoneNumberModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']
    list_editable = ['phone_number']


admin.site.register(UserPhoneNumber, PhoneNumberModelAdmin)

admin.site.site_header = 'MineCraft Pay'
admin.site.site_title = f'پنل ادمین وبسایت'
admin.site.index_title = admin.site.site_header