# Generated by Django 4.1.5 on 2023-07-17 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_subscription_order_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.subscription')),
            ],
        ),
    ]
