# Generated by Django 4.1.3 on 2022-12-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_excelcartreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='excelcartreview',
            name='image',
            field=models.ImageField(null=True, upload_to='testimonials'),
        ),
    ]
