# Generated by Django 2.2.19 on 2021-04-28 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icecream', '0006_delete_favourite_icecream'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ice_cream',
            options={'ordering': ['-id']},
        ),
    ]