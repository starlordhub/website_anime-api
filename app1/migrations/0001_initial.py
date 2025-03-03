# Generated by Django 5.1.3 on 2025-01-27 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('ongoing', 'Ongoing'), ('completed', 'Completed'), ('upcoming', 'Upcoming')], max_length=10)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('image_url', models.URLField(blank=True, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
