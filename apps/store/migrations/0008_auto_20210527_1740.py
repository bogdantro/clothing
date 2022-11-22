# Generated by Django 3.1.5 on 2021-05-27 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category'),
        ),
    ]
