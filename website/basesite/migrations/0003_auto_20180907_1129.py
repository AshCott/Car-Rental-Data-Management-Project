# Generated by Django 2.1 on 2018-09-07 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basesite', '0002_auto_20180907_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(max_length=25),
        ),
    ]
