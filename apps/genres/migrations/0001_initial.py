# Generated by Django 5.0.1 on 2024-06-08 03:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demographic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True, verbose_name='is available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated at')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'demographic',
                'verbose_name_plural': 'demographics',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True, verbose_name='is available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated at')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True, verbose_name='is available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated at')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'theme',
                'verbose_name_plural': 'themes',
                'ordering': ['pk'],
            },
        ),
    ]
