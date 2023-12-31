# Generated by Django 4.2.7 on 2023-11-17 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_carrito_producto_carrito_contador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrito',
            old_name='contador',
            new_name='contador_productos',
        ),
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(to='myapp.producto'),
        ),
        migrations.CreateModel(
            name='SolicitudCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrito', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.carrito')),
            ],
        ),
    ]
