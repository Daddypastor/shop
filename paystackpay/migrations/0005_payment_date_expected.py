# Generated by Django 4.1.3 on 2022-11-29 13:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paystackpay', '0004_alter_payment_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='date_expected',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
