from django.shortcuts import render
from posts.models import Post
from posts.tests import set_up

def main_view(request):
    set_up()
    post = Post.objects.all()[0]
    return render(request, 'main.html', {'post':post})
