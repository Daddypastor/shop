# Generated by Django 4.1.3 on 2022-11-17 23:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, null=True)),
                ('expiry_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
