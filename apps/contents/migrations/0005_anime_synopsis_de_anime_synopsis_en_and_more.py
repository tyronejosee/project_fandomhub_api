# Generated by Django 5.0.1 on 2024-03-06 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_anime_name_rom_manga_name_rom_alter_anime_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='synopsis_de',
            field=models.TextField(blank=True, null=True, verbose_name='Synopsis'),
        ),
        migrations.AddField(
            model_name='anime',
            name='synopsis_en',
            field=models.TextField(blank=True, null=True, verbose_name='Synopsis'),
        ),
        migrations.AddField(
            model_name='anime',
            name='synopsis_es',
            field=models.TextField(blank=True, null=True, verbose_name='Synopsis'),
        ),
        migrations.AddField(
            model_name='anime',
            name='synopsis_fr',
            field=models.TextField(blank=True, null=True, verbose_name='Synopsis'),
        ),
        migrations.AddField(
            model_name='anime',
            name='synopsis_it',
            field=models.TextField(blank=True, null=True, verbose_name='Synopsis'),
        ),
        migrations.AddField(
            model_name='anime',
            name='synopsis_ja',
            field=models.TextField(blank=True, null=True, verbose_name='Synopsis'),
        ),
        migrations.AddField(
            model_name='anime',
            name='synopsis_pt',
            field=models.TextField(blank=True, null=True, verbose_name='Synopsis'),
        ),
    ]