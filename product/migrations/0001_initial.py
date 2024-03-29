# Generated by Django 4.1.3 on 2022-11-15 15:26

import ckeditor.fields
import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('short', models.CharField(max_length=100, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('main_image', models.ImageField(null=True, upload_to='product_img/')),
                ('ref', models.CharField(blank=True, max_length=100, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('side_image', models.ImageField(blank=True, null=True, upload_to='product_img/')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('new', models.BooleanField(default=False)),
                ('top_deals', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subcategory')),
            ],
            options={
                'verbose_name_plural': 'Product',
            },
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_status', models.CharField(choices=[('1', 'In Stock'), ('2', 'Out Of Stock'), ('3', 'Pre-order')], default='In Stock', max_length=150)),
                ('number', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('size_par', models.CharField(blank=True, choices=[('KG', 'kilogramme'), ('G', 'gramme'), ('XL', 'extra-large')], default='kilogramme', max_length=150, null=True)),
                ('size', models.CharField(max_length=100, null=True)),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=[('#FFFFFF', 'white'), ('#000000', 'black'), ('#FF0000', 'red'), ('#00FF00 ', 'green'), ('#FFFF00', 'yellow'), ('#0000FF', 'blue')])),
                ('price', models.FloatField(default=0, null=True)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='product_img/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name_plural': 'Variations',
            },
        ),
    ]
