# Generated by Django 4.1.3 on 2022-11-18 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponcode',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
