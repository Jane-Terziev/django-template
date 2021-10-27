from ..app_models.post import Post


class PostService:
    def __init__(self, post_repository=Post):
        self.post_repository = post_repository

    def create_post(self, data):
        post = self.post_repository.create_new(title=data["title"], body=data["body"])
        post.save()


    def update_post(self, data):
        self.post_repository.get_object_or_404(data['id'])






