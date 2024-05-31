# Generated by Django 5.0.1 on 2024-05-31 18:41

import apps.utils.paths
import apps.utils.validators
import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('genres', '0001_initial'),
        ('seasons', '0001_initial'),
        ('studios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True, verbose_name='available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated at')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name (eng)')),
                ('name_jpn', models.CharField(max_length=255, unique=True, verbose_name='name (jpn)')),
                ('name_rom', models.CharField(blank=True, max_length=255, unique=True, verbose_name='name (rmj)')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.utils.paths.image_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'webp']), apps.utils.validators.ImageSizeValidator(max_height=1280, max_width=909), apps.utils.validators.FileSizeValidator(limit_mb=2)], verbose_name='image')),
                ('synopsis', models.TextField(blank=True, null=True, verbose_name='synopsis')),
                ('episodes', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1500)], verbose_name='episodes')),
                ('duration', models.CharField(blank=True, max_length=20, null=True, verbose_name='duration')),
                ('release', models.DateField(blank=True, null=True, verbose_name='release')),
                ('category', models.CharField(choices=[('pending', 'Pending'), ('tv', 'TV'), ('ova', 'OVA'), ('movie', 'Movie'), ('special', 'Special'), ('ona', 'ONA'), ('music', 'Music')], default='pending', max_length=10, verbose_name='category')),
                ('website', models.URLField(blank=True, max_length=255)),
                ('trailer', models.URLField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('finished', 'Finished'), ('airing', 'Airing'), ('upcoming', 'Upcoming')], default='pending', max_length=10, verbose_name='status')),
                ('rating', models.CharField(choices=[('pending', 'Pending'), ('g', 'G - All Ages'), ('pg', 'PG - Children'), ('pg13', 'PG-13 - Teens 13 and Older'), ('r', 'R - 17+ (Violence & Profanity)'), ('rplus', 'R+ - Profanity & Mild Nudity'), ('rx', 'RX - Hentai')], default='pending', max_length=10, verbose_name='rating')),
                ('mean', models.FloatField(blank=True, null=True, verbose_name='mean')),
                ('rank', models.IntegerField(blank=True, null=True, verbose_name='rank')),
                ('popularity', models.IntegerField(blank=True, null=True, verbose_name='popularity')),
                ('favorites', models.IntegerField(blank=True, default=0, null=True, verbose_name='favorites')),
                ('num_list_users', models.IntegerField(blank=True, default=0, null=True, verbose_name='number of list users')),
                ('genres', models.ManyToManyField(blank=True, to='genres.genre')),
                ('season', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seasons.season')),
                ('studio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studios.studio')),
                ('themes', models.ManyToManyField(blank=True, to='categories.theme')),
            ],
            options={
                'verbose_name': 'anime',
                'verbose_name_plural': 'animes',
                'ordering': ['pk'],
            },
        ),
    ]