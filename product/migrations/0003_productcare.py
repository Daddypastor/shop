# Generated by Django 4.1.3 on 2022-11-15 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('care', models.CharField(max_length=500, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name_plural': 'Product care',
            },
        ),
    ]
