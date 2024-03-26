# Generated by Django 5.0.1 on 2024-03-26 15:53

import apps.utils.paths
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demographic',
            options={'verbose_name': 'demographic', 'verbose_name_plural': 'demographics'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'genre', 'verbose_name_plural': 'genres'},
        ),
        migrations.AlterModelOptions(
            name='season',
            options={'verbose_name': 'season', 'verbose_name_plural': 'season'},
        ),
        migrations.AlterModelOptions(
            name='studio',
            options={'verbose_name': 'studio', 'verbose_name_plural': 'studios'},
        ),
        migrations.AlterModelOptions(
            name='theme',
            options={'verbose_name': 'theme', 'verbose_name_plural': 'themes'},
        ),
        migrations.AlterField(
            model_name='demographic',
            name='available',
            field=models.BooleanField(db_index=True, default=True, verbose_name='available'),
        ),
        migrations.AlterField(
            model_name='demographic',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='demographic',
            name='name',
            field=models.CharField(db_index=True, max_length=50, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='demographic',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='available',
            field=models.BooleanField(db_index=True, default=True, verbose_name='available'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='season',
            name='available',
            field=models.BooleanField(db_index=True, default=True, verbose_name='available'),
        ),
        migrations.AlterField(
            model_name='season',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='season',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='season',
            name='season',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Winter'), (2, 'Spring'), (3, 'Summer'), (4, 'Fall')], default=0, verbose_name='season'),
        ),
        migrations.AlterField(
            model_name='season',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='season',
            name='year',
            field=models.IntegerField(db_index=True, default=2010, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2100)], verbose_name='year'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='available',
            field=models.BooleanField(db_index=True, default=True, verbose_name='available'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='established',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='established'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.utils.paths.image_path, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='name (eng)'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='name_jpn',
            field=models.CharField(max_length=255, unique=True, verbose_name='name (jpn)'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='available',
            field=models.BooleanField(db_index=True, default=True, verbose_name='available'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
    ]
