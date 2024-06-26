# Generated by Django 5.0.1 on 2024-06-08 03:52

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
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True, verbose_name='is available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated at')),
                ('object_id', models.UUIDField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='rating')),
                ('comment', models.TextField(verbose_name='comment')),
                ('is_spoiler', models.BooleanField(default=False, verbose_name='is spoiler')),
                ('helpful_count', models.PositiveIntegerField(default=0, verbose_name='helpful count')),
                ('reported_count', models.PositiveIntegerField(default=0, verbose_name='reported count')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user_id', models.ForeignKey(limit_choices_to={'is_available': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews',
                'ordering': ['-created_at'],
                'unique_together': {('content_type', 'object_id', 'user_id')},
            },
        ),
    ]
