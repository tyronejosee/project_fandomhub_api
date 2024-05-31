# Generated by Django 5.0.1 on 2024-05-31 21:44

import apps.utils.paths
import apps.utils.validators
import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animes', '0001_initial'),
        ('mangas', '0001_initial'),
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True, verbose_name='available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated at')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('name_kanji', models.CharField(max_length=255, verbose_name='name kanji')),
                ('favorites', models.PositiveIntegerField(default=0, verbose_name='favorites')),
                ('about', models.TextField(blank=True, verbose_name='about')),
                ('role', models.CharField(choices=[('main', 'Main'), ('supporting', 'Supporting')], max_length=15, verbose_name='role')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.utils.paths.image_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['webp']), apps.utils.validators.ImageSizeValidator(max_height=600, max_width=600), apps.utils.validators.FileSizeValidator(limit_mb=1)], verbose_name='image')),
            ],
            options={
                'verbose_name': 'character',
                'verbose_name_plural': 'characters',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='CharacterAnime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_anime', to='animes.anime')),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_anime', to='characters.character')),
            ],
            options={
                'verbose_name': 'character anime',
                'verbose_name_plural': 'character animes',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='CharacterManga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_manga', to='characters.character')),
                ('manga_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_manga', to='mangas.manga')),
            ],
            options={
                'verbose_name': 'character manga',
                'verbose_name_plural': 'character mangas',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='CharacterVoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True, verbose_name='available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated at')),
                ('language', models.CharField(choices=[('japanese', 'Japanese'), ('english', 'English'), ('spanish', 'Spanish'), ('french', 'French'), ('german', 'German'), ('italian', 'Italian'), ('portuguese', 'Portuguese')], default='japanese', max_length=20, verbose_name='language')),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_voice', to='characters.character')),
                ('voice_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='character_voice', to='persons.person')),
            ],
            options={
                'verbose_name': 'character voice',
                'verbose_name_plural': 'character voices',
                'ordering': ['pk'],
            },
        ),
    ]