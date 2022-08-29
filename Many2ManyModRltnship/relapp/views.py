from django.shortcuts import render
from .models import Song

# Create your views here.

def index(request):
    # songs = Song.objects.all()
    songs = Song.objects.prefetch_related('user').all()
    # temp = {}
    # i=1
    # for song in songs:
    #     temp[i] = song
    # print(temp)
    return render(request, 'index.html', context={'temp':songs})