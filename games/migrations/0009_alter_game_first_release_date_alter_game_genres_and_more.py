# Generated by Django 4.1.1 on 2022-10-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_game_first_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='first_release_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(blank=True, related_name='games', to='games.genre'),
        ),
        migrations.AlterField(
            model_name='game',
            name='platforms',
            field=models.ManyToManyField(blank=True, related_name='games', to='games.platform'),
        ),
    ]
