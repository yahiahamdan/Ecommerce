# Generated by Django 5.0.6 on 2024-06-15 23:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_postal_code_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='123456789012', max_length=12, validators=[django.core.validators.RegexValidator('^\\d{12}$')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=300),
        ),
    ]