from djongo import models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(default="", max_length=100)
    body = models.CharField(default="", max_length=100)

    objects = models.DjongoManager()

    @classmethod
    def create_new(cls, title, body):
        return cls(
            title=title,
            body=body
        )

