from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

posts = [
    {
        'author': 'Faysal Ahammed',
        'title': 'Blog Post 1',
        'content': 'First blog content',
        'date': 'June 27, 2023'
    },
    {
        'author': 'Khadi',
        'title': 'Blog Post 2',
        'content': 'Second blog content',
        'date': 'June 27, 2023'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'My_blog/home.html', context)


def about(request):
    return render(request, 'My_blog/about.html', {'title': 'About'})
