# Generated by Django 3.1.7 on 2021-04-01 14:15

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinginvoice',
            name='status',
            field=django_mysql.models.EnumField(choices=[('pending', 'Pending'), ('final', 'Final')]),
        ),
    ]
