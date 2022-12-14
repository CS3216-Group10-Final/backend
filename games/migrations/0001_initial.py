# Generated by Django 4.1.1 on 2022-10-07 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('cover', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GameEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True)),
                ('review', models.TextField(blank=True)),
                ('hours', models.IntegerField(blank=True)),
                ('is_favourite', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(0, 'Wishlist'), (1, 'Backlog'), (2, 'Playing'), (3, 'Completed'), (4, 'Dropped')], default=3)),
                ('time_started', models.DateTimeField(blank=True)),
                ('time_completed', models.DateTimeField(blank=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='games.game')),
            ],
        ),
    ]
