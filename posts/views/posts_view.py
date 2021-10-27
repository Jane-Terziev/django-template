from django.shortcuts import render
from django.http import HttpResponseRedirect
from posts.forms.posts.post_create_form import PostCreateForm
from posts.forms.posts.post_update_form import PostUpdateForm
from posts.services.post_service import PostService
from posts.services.post_read_service import PostReadService


def index(request):
    posts = PostReadService().get_posts()
    return render(request, 'posts/index_posts.html', {'posts': posts})


def create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            PostService().create_post(form.cleaned_data)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'posts/create_posts.html', {'form': form}, status=422)
    else:
        return render(request, 'posts/create_posts.html', {'form': PostCreateForm()})


def edit(request, id):
    if request.method == 'POST':
        form = PostUpdateForm(request.POST)
        if form.is_valid():
            PostService().update_post(form.cleaned_data)
            return HttpResponseRedirect("/")
        else:
            return render(request, 'posts/edit_posts.html', context={'form': form})
    else:
        form = PostUpdateForm()
        form.initial['id'] = id
        return render(request, 'posts/edit_posts.html', context={'form': form})
