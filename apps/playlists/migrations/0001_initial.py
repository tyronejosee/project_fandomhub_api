# Generated by Django 5.0.1 on 2024-05-31 18:41

import apps.utils.paths
import apps.utils.validators
import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True, verbose_name='available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('number_items', models.IntegerField(default=0, verbose_name='number of items')),
                ('cover', models.ImageField(blank=True, null=True, upload_to=apps.utils.paths.image_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'webp']), apps.utils.validators.ImageSizeValidator(max_height=600, max_width=600), apps.utils.validators.FileSizeValidator(limit_mb=1)], verbose_name='image')),
                ('is_public', models.BooleanField(default=True, verbose_name='is public')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'playlist',
                'verbose_name_plural': 'playlists',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='PlaylistItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True, verbose_name='available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated at')),
                ('object_id', models.UUIDField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('watching', 'Watching'), ('completed', 'Completed'), ('on_hold', 'On Hold'), ('dropped', 'Dropped'), ('plan_watch', 'Plan to Watch')], db_index=True, default='pending', max_length=20, verbose_name='status')),
                ('is_watched', models.BooleanField(db_index=True, default=False, verbose_name='is watched')),
                ('is_favorite', models.BooleanField(db_index=True, default=False, verbose_name='is favorite')),
                ('order', models.FloatField(default=0)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlists.playlist', verbose_name='playlist')),
            ],
            options={
                'verbose_name': 'playlist item',
                'verbose_name_plural': 'playlist items',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True, verbose_name='available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'ordering': ['pk'],
            },
        ),
        migrations.AddField(
            model_name='playlist',
            name='tags',
            field=models.ManyToManyField(blank=True, to='playlists.tag', verbose_name='tags'),
        ),
    ]
