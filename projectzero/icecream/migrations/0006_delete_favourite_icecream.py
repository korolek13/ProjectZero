# Generated by Django 2.2.19 on 2021-04-24 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icecream', '0005_ice_cream_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favourite_icecream',
        ),
    ]