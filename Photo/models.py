from django.db import models


class ImageCard(models.Model):
    image_url = models.CharField(max_length=2048)
    title = models.CharField(max_length=32)
    subtitle = models.CharField(max_length=60)
    share_link = models.CharField(max_length=2048)
