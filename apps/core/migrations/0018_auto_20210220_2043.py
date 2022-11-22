# Generated by Django 3.1.5 on 2021-02-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Gaming', 'G'), ('Bogdan', 'BO'), ('Test', 'T')], max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Gaming', 'G'), ('Bogdan', 'BO'), ('Test', 'T')], max_length=60),
        ),
    ]
