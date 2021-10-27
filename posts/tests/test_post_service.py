from unittest.mock import MagicMock
from posts.app_models.post import Post
from ..services.post_service import PostService
from django.test import TestCase


class PostServiceTest(TestCase):
    def test_create_post(self):
        data = {
            'title': 'title',
            'body': 'body'
        }

        post = Post(title=data['title'], body=data['body'])
        post.save = MagicMock()
        Post.create_new = MagicMock(return_value=post)
        post_service = PostService()

        post_service.create_post(data)

        post.create_new.assert_called_once_with(title=data['title'], body=data['body'])
        post.save.assert_called_once



    def test_update_post_404(self):
        post = Post(title=data['title'], body=data['body'])
        Post.get_object_or_404 = MagicMock()