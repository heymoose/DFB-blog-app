from django.views.generic import ListView, DetailView
from blog.models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
