# Generated by Django 5.0.1 on 2024-06-08 03:52

import apps.utils.paths
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animes', '0001_initial'),
        ('mangas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True, verbose_name='is available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('content', models.TextField(verbose_name='content')),
                ('image', models.ImageField(upload_to=apps.utils.paths.picture_image_path, verbose_name='image')),
                ('source', models.URLField(max_length=255, verbose_name='source')),
                ('tag', models.CharField(choices=[('pending', 'Pending'), ('new_anime', 'New Anime'), ('new_manga', 'New Manga'), ('spoiler', 'Spoiler'), ('review', 'Review'), ('interview', 'Interview'), ('event', 'Event'), ('recommendation', 'Recommendation')], default='pending', max_length=15, verbose_name='tag')),
                ('anime_relations', models.ManyToManyField(blank=True, to='animes.anime')),
                ('author_id', models.ForeignKey(limit_choices_to={'is_available': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('manga_relations', models.ManyToManyField(blank=True, to='mangas.manga')),
            ],
            options={
                'verbose_name': 'news',
                'verbose_name_plural': 'news',
                'ordering': ['pk'],
                'indexes': [models.Index(fields=['name'], name='name_idx'), models.Index(fields=['tag'], name='tag_idx')],
            },
        ),
    ]
