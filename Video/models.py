from django.db import models


class NewVideo(models.Model):
    video_title = models.CharField(max_length=100)
    video_url = models.CharField(max_length=2048)
    background_image = models.CharField(max_length=2048)


class VideoExplanation(models.Model):
    video_subtitle = models.CharField(max_length=100)
    subtitle_explanation = models.TextField()


class MoreVideo(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=2048)
    video_code = models.CharField(max_length=100)



