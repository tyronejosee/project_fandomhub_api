# Generated by Django 5.0.1 on 2024-02-11 02:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_alter_anime_available_alter_manga_available'),
        ('profiles', '0002_animelist'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animelist',
            name='anime',
        ),
        migrations.AlterField(
            model_name='animelist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='available',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Available'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='available',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Available'),
        ),
        migrations.AddField(
            model_name='animelist',
            name='anime',
            field=models.ManyToManyField(to='contents.anime'),
        ),
    ]