from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Song(models.Model):
    user = models.ManyToManyField(User)
    song_title = models.CharField(max_length=100)
    song_duration = models.IntegerField()

    def __str__(self):
        return self.song_title

    def song_sung_by(self):
        return ', '.join([str(p) for p in self.user.all()])