# Generated by Django 4.1.1 on 2022-10-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_alter_game_first_release_date_alter_game_genres_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]