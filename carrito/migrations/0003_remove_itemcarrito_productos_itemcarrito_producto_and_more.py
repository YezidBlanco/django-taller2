# Generated by Django 5.0.7 on 2024-07-25 04:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_itemcarrito_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcarrito',
            name='productos',
        ),
        migrations.AddField(
            model_name='itemcarrito',
            name='producto',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='carrito.producto'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('productos', models.ManyToManyField(through='carrito.ItemCarrito', to='carrito.producto')),
            ],
        ),
        migrations.AddField(
            model_name='itemcarrito',
            name='carrito',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='carrito.carrito'),
            preserve_default=False,
        ),
    ]
