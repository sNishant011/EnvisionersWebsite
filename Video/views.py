from django.shortcuts import render
from .models import NewVideo, VideoExplanation, MoreVideo
from Home.models import About


def index(request):
    videos = NewVideo.objects.all()
    abouts = About.objects.all()
    more_videos = MoreVideo.objects.all()
    explanations = VideoExplanation.objects.all()
    return render(request, 'videos.html', {'videos': videos,
                                           'abouts': abouts,
                                           'explanations': explanations,
                                           'more_videos': more_videos})
