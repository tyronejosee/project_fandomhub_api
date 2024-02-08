# Generated by Django 5.0.1 on 2024-02-08 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='users', to='users.role'),
        ),
    ]
