# Generated by Django 3.2.21 on 2023-09-16 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0009_auto_20230916_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkitem',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tapasitem',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
