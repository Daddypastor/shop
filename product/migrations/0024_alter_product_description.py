# Generated by Django 4.1.3 on 2023-02-08 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_product_avg_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
