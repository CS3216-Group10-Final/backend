# Generated by Django 4.1.1 on 2022-10-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_alter_platform_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(related_name='games', to='games.genre'),
        ),
        migrations.AddField(
            model_name='game',
            name='platforms',
            field=models.ManyToManyField(related_name='games', to='games.platform'),
        ),
    ]