# Generated by Django 4.1.5 on 2023-07-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pool',
            name='is_busy',
            field=models.BooleanField(default=False),
        ),
    ]
