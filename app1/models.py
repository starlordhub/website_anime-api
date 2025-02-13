from django.db import models

# Create your models here.

from django.db import models

class Anime(models.Model):
    CATEGORY_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('upcoming', 'Upcoming'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    image_url = models.URLField(blank=True, null=True)  # Optional image for the anime
    video_url = models.URLField(blank=True, null=True)  # URL to the video page
    link = models.URLField(default='', blank=True)

    def __str__(self):
        return self.title

