# Generated by Django 4.2.6 on 2023-10-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainsitesettings',
            options={'verbose_name': 'تنظیمات وبسایت', 'verbose_name_plural': 'تنظیمات وبسایت'},
        ),
        migrations.AlterModelOptions(
            name='signupsettings',
            options={'verbose_name': 'تنظیمات صفحه ورود به حساب کاربری', 'verbose_name_plural': 'تنظیمات صفحه ورود به حساب کاربری'},
        ),
        migrations.RemoveField(
            model_name='signupsettings',
            name='page_button_S',
        ),
        migrations.AddField(
            model_name='signupsettings',
            name='page_button_color',
            field=models.CharField(choices=[('btn btn-success', '🟢 سبز'), ('btn btn-link', '🟦 آبی روشن'), ('btn btn-primary', '🔵 آبی تیره'), ('btn btn-warning', '🟡 زرد'), ('btn btn-danger', '🔴 قرمز')], default='🟦 آبی روشن', max_length=150, verbose_name='رنگبندی دکمه'),
        ),
        migrations.AlterField(
            model_name='signupsettings',
            name='page_confirm_password_input_hint',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='نوشته ورودی تایید رمز ورود'),
        ),
        migrations.AlterField(
            model_name='signupsettings',
            name='page_confirm_password_input_placeholder',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='نوشته موقت ورودی تایید رمز ورود'),
        ),
        migrations.AlterField(
            model_name='signupsettings',
            name='page_email_input_hint',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='نوشته ورودی ایمیل'),
        ),
        migrations.AlterField(
            model_name='signupsettings',
            name='page_email_input_placeholder',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='نوشته موقت ورودی ایمیل'),
        ),
        migrations.AlterField(
            model_name='signupsettings',
            name='page_fname_input_hint',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='نوشته ورودی نام'),
        ),
        migrations.AlterField(
            model_name='signupsettings',
            name='page_fname_input_placeholder',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='نوشته موقت ورودی نام'),
        ),
        migrations.AlterField(
            model_name='signupsettings',
            name='page_lname_input_hint',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='نوشته ورودی نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='signupsettings',
            name='page_lname_input_placeholder',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='نوشته موقت ورودی نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='signupsettings',
            name='page_password_input_hint',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='نوشته ورودی رمز ورود'),
        ),
        migrations.AlterField(
            model_name='signupsettings',
            name='page_password_input_placeholder',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='نوشته موقت ورودی رمز ورود'),
        ),
    ]
