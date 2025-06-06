# Generated by Django 5.1.7 on 2025-05-27 05:09

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(10.0, message='Amount must be at least ₹10.')]),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donor_account_no',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='Account number should be 8 to 20 digits.', regex='^\\d{8,20}$')]),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donor_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Name should contain only letters and spaces.', regex='^[a-zA-Z\\s]+$')]),
        ),
    ]
