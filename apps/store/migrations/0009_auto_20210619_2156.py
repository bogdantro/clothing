# Generated by Django 3.1.5 on 2021-06-19 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20210527_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='is_featured',
            new_name='is_home_page',
        ),
    ]