# Generated by Django 2.2.19 on 2022-09-11 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]