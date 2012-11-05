from django.shortcuts import render
from news.models import Post

def news_view(request):
    posts = Post.objects.filter(visible=True).order_by('date')
    return render(request, 'news.html', {'posts':posts})