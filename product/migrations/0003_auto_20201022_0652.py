# Generated by Django 3.1.2 on 2020-10-22 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_color_hex_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
