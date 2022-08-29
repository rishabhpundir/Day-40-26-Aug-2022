from django.shortcuts import render
from .models import Author, Course

# Create your views here.

def index(request):
    courses = Course.objects.select_related('author').all()
    temp = {}
    i=1
    for course in courses:
        temp[i] = course
        i+=1
    return render(request, 'index.html', context={'temp':temp})