# Generated by Django 3.1.2 on 2020-10-27 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_address_is_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='is_default',
            field=models.SmallIntegerField(default=0),
        ),
    ]
