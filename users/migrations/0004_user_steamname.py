# Generated by Django 4.1.1 on 2022-10-30 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='steamname',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]