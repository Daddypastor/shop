# Generated by Django 4.1.3 on 2022-12-30 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paystackpay', '0008_payment_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='discount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]