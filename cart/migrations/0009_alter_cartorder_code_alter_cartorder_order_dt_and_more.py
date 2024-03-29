# Generated by Django 4.1.3 on 2022-12-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_cartorder_code_tracking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='order_dt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='order_status',
            field=models.CharField(choices=[('process', 'In Process'), ('delivered', 'Delivered')], default='process', max_length=150),
        ),
    ]
