# Generated by Django 5.2.3 on 2025-07-15 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sing', '0006_remove_song_image_singer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('writer', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='sing.singer')),
            ],
        ),
    ]
