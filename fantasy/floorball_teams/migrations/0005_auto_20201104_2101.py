# Generated by Django 3.1.2 on 2020-11-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floorball_teams', '0004_auto_20200928_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='floorballteam',
            name='new_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='floorballteam',
            name='old_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
