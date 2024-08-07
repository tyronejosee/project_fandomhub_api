# Generated by Django 5.0.1 on 2024-07-02 21:00

import apps.utils.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0004_mangalistitem_unique_mangalist_manga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animelist',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='playlists/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'webp']), apps.utils.validators.ImageSizeValidator(max_height=1500, max_width=500), apps.utils.validators.FileSizeValidator(limit_mb=1)], verbose_name='banner'),
        ),
        migrations.AlterField(
            model_name='mangalist',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='playlists/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'webp']), apps.utils.validators.ImageSizeValidator(max_height=1500, max_width=500), apps.utils.validators.FileSizeValidator(limit_mb=1)], verbose_name='banner'),
        ),
    ]
