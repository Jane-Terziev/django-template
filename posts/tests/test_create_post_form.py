from django.test import TestCase
from posts.forms.posts.post_create_form import PostCreateForm

data = {'title': 'title', 'body': 'body'}

class PostCreateFormTest(TestCase):
    def test_is_valid_false_when_title_is_missing(self):
        params = {k:v for k,v in data.items() if k not in {'title'}}
        self.assertEquals(PostCreateForm(params).is_valid(), False)

    def test_is_valid_false_when_body_is_missing(self):
        params = {k:v for k,v in data.items() if k not in {'body'}}
        self.assertEquals(PostCreateForm(params).is_valid(), False)

    def test_is_valid_false_when_title_greater_than_max_length(self):
        params = data.copy()
        params['title'] = 'a' * 101
        self.assertEquals(PostCreateForm(params).is_valid(), False)

    def test_is_valid_false_when_body_greater_than_max_length(self):
        params = data.copy()
        params['body'] = 'a' * 1001
        self.assertEquals(PostCreateForm(params).is_valid(), False)

    def test_is_valid_false_when_title_is_empty_string(self):
        params = data.copy()
        params['title'] = ''
        self.assertEquals(PostCreateForm(params).is_valid(), False)

    def test_is_valid_false_when_body_is_empty_string(self):
        params = data.copy()
        params['body'] = ''
        self.assertEquals(PostCreateForm(params).is_valid(), False)

    def test_is_valid_true_when_parameters_are_valid(self):
        self.assertEquals(PostCreateForm(data).is_valid(), True)