# Generated by Django 3.1.2 on 2020-10-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201022_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='product',
            field=models.ManyToManyField(through='product.ProductTag', to='product.Product'),
        ),
    ]