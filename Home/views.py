from django.shortcuts import render
from .models import ImageCard, About


def index(request):
    cards = ImageCard.objects.all()
    abouts = About.objects.all()
    return render(request, 'index.html', {'cards': cards,
                                          'abouts': abouts,
                                          'cssfile': 'index',
                                          'welcomemsg': 'Hello Envisioners',
                                          'title': 'Home | Envisioners',
                                        })
