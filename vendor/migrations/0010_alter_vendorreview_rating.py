# Generated by Django 4.1.3 on 2022-12-23 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0009_alter_vendorreview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorreview',
            name='rating',
            field=models.IntegerField(choices=[('1', '1 Star'), ('2', '2 Stars'), ('3', '3 Stars'), ('4', '4 Stars'), ('5', '5 Stars')], default=1),
        ),
    ]
