# Generated by Django 4.2.7 on 2023-11-18 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_solicitud'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='productos',
            field=models.CharField(default='', max_length=100),
        ),
    ]