# Generated by Django 4.1.1 on 2022-10-08 21:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_game_genres_game_platforms'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='first_release_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]