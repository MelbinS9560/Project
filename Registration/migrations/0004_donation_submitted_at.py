# Generated by Django 5.1.7 on 2025-05-27 16:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_donation_donor'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
