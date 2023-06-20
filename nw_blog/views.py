from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# def index(request):
#     return render(request, 'index.html', {})

class IndexView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_view.html'

class CreatePostView(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = '__all__'