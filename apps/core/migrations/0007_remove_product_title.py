# Generated by Django 3.1.5 on 2021-02-13 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_product_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
    ]
