from django.test import TestCase
from posts.app_models.post import Post



class PostModelTest(TestCase):
    def test_create_new(self):
        title = 'Title'
        body = 'Body'
        post = Post.create_new(title=title, body=body)
        self.assertEqual(post.title, title)
        self.assertEqual(post.body, body)
