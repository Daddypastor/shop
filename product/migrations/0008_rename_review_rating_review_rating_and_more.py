# Generated by Django 4.1.3 on 2022-11-15 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_review_date_alter_review_review_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_rating',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='review_text',
            new_name='text',
        ),
    ]
