# Generated by Django 4.1.3 on 2022-11-19 04:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0005_alter_customeraddress_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=11, null=True)),
                ('Order_notes', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('customer', models.CharField(blank=True, max_length=300, null=True)),
                ('amount', models.CharField(max_length=100)),
                ('payment_option', models.TextField(choices=[('Cash', 'Cash On Delivery'), ('Transfer', 'Direct Bank Transfer'), ('Paystack', 'Pay Online [Secured]')], default='Cash')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('verified', models.BooleanField(default=False, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.customeraddress')),
            ],
            options={
                'verbose_name_plural': 'Payment',
            },
        ),
    ]
