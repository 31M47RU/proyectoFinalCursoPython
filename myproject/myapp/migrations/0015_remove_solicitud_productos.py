# Generated by Django 4.2.7 on 2023-11-18 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_solicitud_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='productos',
        ),
    ]
