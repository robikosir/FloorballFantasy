# Generated by Django 3.1.1 on 2020-10-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_team_goalie'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='budget',
            field=models.IntegerField(default=1000000),
        ),
    ]
