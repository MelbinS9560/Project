# Generated by Django 5.1.7 on 2025-05-27 05:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0002_alter_donation_mobile_alter_donation_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='registration_donations', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
