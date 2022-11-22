# Generated by Django 3.1.5 on 2021-02-13 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_product_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price_in_dollars',
        ),
    ]
