# Generated by Django 4.1.5 on 2023-07-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_pool_is_busy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shorts',
            new_name='shorts_number',
        ),
        migrations.AddField(
            model_name='order',
            name='debt',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='is_subscribed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='summ',
            field=models.CharField(max_length=50),
        ),
    ]