# Generated by Django 2.2 on 2021-02-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ice_cream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('avatar', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
