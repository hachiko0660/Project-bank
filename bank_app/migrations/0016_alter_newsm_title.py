# Generated by Django 4.2.2 on 2023-07-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0015_remove_newsm_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsm',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
