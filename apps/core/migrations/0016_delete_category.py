# Generated by Django 3.1.5 on 2021-02-20 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]