from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post



class IndexView(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_view.html'

class CreatePostView(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = '__all__'
