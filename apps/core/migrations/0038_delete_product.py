# Generated by Django 3.1.5 on 2021-03-11 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20210311_1545'),
        ('order', '0002_auto_20210311_1545'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
