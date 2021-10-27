from django.urls import path
from .views.posts_view import (
    index,
    create,
    edit,
)

app_name = 'posts'
urlpatterns = [
    path('', index, name='index_posts'),
    path('posts/create/', create, name='create_post'),
    path('posts/<id>/edit', edit, name='edit_post'),
]
