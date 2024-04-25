# Generated by Django 5.0.1 on 2024-04-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_alter_anime_category_alter_anime_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='num_list_users',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='number of list users'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='num_scoring_users',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='number of scoring users'),
        ),
    ]