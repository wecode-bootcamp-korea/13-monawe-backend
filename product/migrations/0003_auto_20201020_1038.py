# Generated by Django 3.1.2 on 2020-10-20 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20201020_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]