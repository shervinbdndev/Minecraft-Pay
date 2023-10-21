# Generated by Django 4.2.6 on 2023-10-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainSiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_title', models.CharField(blank=True, max_length=64, null=True, verbose_name='عنوان وبسایت')),
                ('website_header', models.CharField(blank=True, max_length=64, null=True, verbose_name='سرتیتر وبسایت')),
            ],
            options={
                'verbose_name': 'تنظیمات وبسایت',
            },
        ),
        migrations.CreateModel(
            name='SignUpSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(blank=True, max_length=64, null=True, verbose_name='عنوان صفحهه')),
                ('page_header', models.CharField(blank=True, max_length=64, null=True, verbose_name='سرتیتر صفحهه')),
                ('page_username_input_hint', models.CharField(blank=True, max_length=64, null=True, verbose_name='نوشته ورودی نام کاربری')),
                ('page_username_input_placeholder', models.CharField(blank=True, max_length=128, null=True, verbose_name='نوشته موقت ورودی نام کاربری')),
                ('page_fname_input_hint', models.CharField(blank=True, max_length=64, null=True, verbose_name='نوشته ورودی نام کاربری')),
                ('page_fname_input_placeholder', models.CharField(blank=True, max_length=128, null=True, verbose_name='نوشته موقت ورودی نام کاربری')),
                ('page_lname_input_hint', models.CharField(blank=True, max_length=64, null=True, verbose_name='نوشته ورودی نام کاربری')),
                ('page_lname_input_placeholder', models.CharField(blank=True, max_length=128, null=True, verbose_name='نوشته موقت ورودی نام کاربری')),
                ('page_email_input_hint', models.CharField(blank=True, max_length=64, null=True, verbose_name='نوشته ورودی نام کاربری')),
                ('page_email_input_placeholder', models.CharField(blank=True, max_length=128, null=True, verbose_name='نوشته موقت ورودی نام کاربری')),
                ('page_password_input_hint', models.CharField(blank=True, max_length=64, null=True, verbose_name='نوشته ورودی نام کاربری')),
                ('page_password_input_placeholder', models.CharField(blank=True, max_length=128, null=True, verbose_name='نوشته موقت ورودی نام کاربری')),
                ('page_confirm_password_input_hint', models.CharField(blank=True, max_length=64, null=True, verbose_name='نوشته ورودی نام کاربری')),
                ('page_confirm_password_input_placeholder', models.CharField(blank=True, max_length=128, null=True, verbose_name='نوشته موقت ورودی نام کاربری')),
                ('page_button_text', models.CharField(blank=True, max_length=32, null=True, verbose_name='نوشته دکمه')),
                ('page_button_S', models.IntegerField(choices=[('🟢', 'btn btn-success'), ('🟦', 'btn btn-info'), ('🔵', 'btn btn-primary'), ('🟡', 'btn btn-warning'), ('🔴', 'btn btn-danger')], default='btn btn-info', verbose_name='رنگبندی دکمه')),
            ],
            options={
                'verbose_name': 'تنظیمات صفحه ورود به حساب کاربری',
            },
        ),
    ]
