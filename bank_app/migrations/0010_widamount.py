# Generated by Django 4.2.2 on 2023-07-10 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0009_rename_amount1_addamount_amount2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='widamount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount1', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
