# Generated by Django 4.0.3 on 2022-03-04 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0002_song_lyrics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='times_played',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
