# Generated by Django 4.1.3 on 2023-03-30 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_faq_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='sate',
        ),
        migrations.AddField(
            model_name='city',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.state'),
        ),
    ]
