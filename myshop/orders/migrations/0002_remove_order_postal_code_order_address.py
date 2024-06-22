# Generated by Django 5.0.6 on 2024-06-15 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='address is required', max_length=300),
        ),
    ]