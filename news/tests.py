"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

from django.test import TestCase
from news.models import Post

def set_up():
    post = Post(heading='Apply for membership',
                body="It's worth it"
                )
    post.save()


class PostTest(TestCase):
    def setUp(self):
        set_up()

    def test_post_created(self):
        p = Post.objects.all()[0]
        self.assertTrue('Apply' in p.heading)
