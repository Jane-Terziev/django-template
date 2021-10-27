from ..app_models.post import Post


class PostReadService:
    def __init__(self, post_repository=Post):
        self.post_repository = post_repository

    def get_posts(self):
        return self.post_repository.objects.all()


