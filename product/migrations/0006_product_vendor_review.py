# Generated by Django 4.1.3 on 2022-11-15 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0005_alter_productinformation_expiry_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('review_rating', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=150)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
