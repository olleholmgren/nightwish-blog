from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, FavouriteAlbum
from .forms import CommentForm, FavouriteAlbumForm


class IndexView(generic.ListView):

    template_name = 'index.html'
    queryset = Post.objects.filter(status=1).order_by('-created_on')

class ConcertMemoriesView(generic.ListView):

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'concert_memories.html'
    paginate_by = 8


class FavouriteAlbumView(generic.CreateView):
    
    model = FavouriteAlbum
    form_class = FavouriteAlbumForm
    template_name = 'favourite_album.html'


class AlbumListView(View):

    def get_album(request):
        if request.method == 'POST':
            form = FavouriteAlbumForm(request.POST)
            if form.is_valid():
                selected_choice = form.cleaned_data['fav_album']
        else:
            form = FavouriteAlbumForm()

        return render(request, 'album_list.html')



class PostDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_view.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_view.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_view', args=[slug]))
