# Generated by Django 4.2.2 on 2023-07-11 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0010_widamount'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=300)),
                ('date', models.DateField()),
            ],
        ),
    ]
