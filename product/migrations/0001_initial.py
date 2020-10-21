<<<<<<< HEAD
# Generated by Django 3.1.2 on 2020-10-21 04:37
=======
# Generated by Django 3.1.2 on 2020-10-21 08:11
>>>>>>> feature/product

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'colors',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'fields',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('price', models.IntegerField()),
                ('origin', models.CharField(max_length=45)),
                ('company', models.CharField(max_length=45)),
<<<<<<< HEAD
                ('create_at', models.DateField()),
                ('updated_at', models.DateField(blank=True, null=True)),
=======
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
>>>>>>> feature/product
                ('description', models.TextField(null=True)),
                ('sales_amount', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='ProductOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(null=True)),
                ('plus_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'product_options',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
=======
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
>>>>>>> feature/product
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Thickness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'thicknesses',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'db_table': 'subcategories',
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='ProductThicknesses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productoption')),
                ('thickness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.thickness')),
            ],
            options={
                'db_table': 'product_thicknesses',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.tag')),
            ],
            options={
                'db_table': 'product_tags',
=======
            name='ProductTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.tag')),
            ],
            options={
                'db_table': 'product_tags',
            },
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(null=True)),
                ('plus_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('etc_option', models.CharField(max_length=50, null=True)),
                ('body_color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='body_color', to='product.color')),
                ('ink_color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ink_color', to='product.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('thickness', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.thickness')),
            ],
            options={
                'db_table': 'product_options',
>>>>>>> feature/product
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=500)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'product_images',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.subcategory'),
<<<<<<< HEAD
        ),
        migrations.CreateModel(
            name='InkColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.color')),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productoption')),
            ],
            options={
                'db_table': 'ink_colors',
            },
=======
>>>>>>> feature/product
        ),
        migrations.AddField(
            model_name='category',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.field'),
        ),
<<<<<<< HEAD
        migrations.CreateModel(
            name='BodyColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.color')),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productoption')),
            ],
            options={
                'db_table': 'body_colors',
            },
        ),
=======
>>>>>>> feature/product
    ]
