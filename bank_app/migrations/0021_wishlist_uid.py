# Generated by Django 4.2.2 on 2023-07-22 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0020_wishlist_newsid'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
