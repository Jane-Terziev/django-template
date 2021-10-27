from django.test import Client, TestCase
from posts.app_models.post import Post


class CreatePostsView(TestCase):
    def test_create_endpoint_success_response_302(self):
        c = Client()
        response = c.post('/posts/create/', {'title': 'Title', 'body': 'Body'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.count(), 1)

    def test_create_endpoint_redirect(self):
        c = Client()
        response = c.post('/posts/create/', {'title': 'Title', 'body': 'Body'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.redirect_chain[-1][0], '/posts/')

    def test_create_endpoint_invalid_parameters_422(self):
        c = Client()
        response = c.post('/posts/create/', {'title': 'Title'})
        self.assertEquals(response.status_code, 422)