# Generated by Django 3.2.21 on 2023-09-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tapasitem',
            name='description',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
