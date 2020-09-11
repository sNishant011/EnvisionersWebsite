from django.db import models


class ImageCard(models.Model):
    image_url = models.CharField(max_length=2048)
    title = models.CharField(max_length=32)
    subtitle = models.CharField(max_length=60)


class About(models.Model):
    aboutline = models.CharField(max_length=5000, default='Some text')
    quote = models.CharField(max_length=5000, default='Some text')
