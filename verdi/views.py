from django.shortcuts import render
from news.models import Post
from news.tests import set_up

def main_view(request):
    set_up()
    post = Post.objects.all()[0]
    return render(request, 'landing.html', {'post':post})
