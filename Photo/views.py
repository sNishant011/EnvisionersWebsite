from django.shortcuts import render
from .models import ImageCard
from Home.models import About


def index(request):
    cards = ImageCard.objects.all()
    abouts = About.objects.all()
    return render(request, 'photos.html', {'cards': cards,
                                           'abouts': abouts,
                                           })
