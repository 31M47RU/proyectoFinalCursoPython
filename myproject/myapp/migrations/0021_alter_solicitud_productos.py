# Generated by Django 4.2.7 on 2023-11-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_solicitud_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='productos',
            field=models.CharField(default='', max_length=100),
        ),
    ]
