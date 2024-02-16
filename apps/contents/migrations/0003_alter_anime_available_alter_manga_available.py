# Generated by Django 5.0.1 on 2024-02-11 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_remove_anime_rating_id_anime_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='available',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Available'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='available',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Available'),
        ),
    ]