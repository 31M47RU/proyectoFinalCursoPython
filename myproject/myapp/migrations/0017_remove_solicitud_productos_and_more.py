# Generated by Django 4.2.7 on 2023-11-18 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_solicitud_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='productos',
        ),
        migrations.AlterField(
            model_name='itemcarrito',
            name='cantidad',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
