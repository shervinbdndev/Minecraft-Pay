from django.contrib import admin
from .models import MainSiteSettings, SignUpSettings



class MainSettingsAdminModel(admin.ModelAdmin):
    list_display = ['website_title', 'website_header']
    
class SignUpSettingsAdminModel(admin.ModelAdmin):
    list_display = ['page_title', 'page_header']
    


admin.site.register(MainSiteSettings, MainSettingsAdminModel)
admin.site.register(SignUpSettings, SignUpSettingsAdminModel)