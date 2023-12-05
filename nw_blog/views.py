from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
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


class AlbumListView(generic.ListView):

    template_name = 'album_list.html'
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    
    def get_album(self, **kwargs):
        
        album = super().get_album(**kwargs)
        album['favourite_album_form'] = FavouriteAlbumForm()
        return album
    
    def post(self, request, *args, **kwargs):

        form = FavouriteAlbumForm(request.POST)
        if form.is_valid():
            selected_choice = form.cleaned_data['favourite_album']
            queryset = Post.objects.filter(status=1, favourite_album=selected_choice).order_by('-created_on')
        else:
            messages.error(request, 'Invalid form submission.')

        album = self.get_context_data()
        album['form'] = form
        return self.render_to_response(album)


        return render(
            request,
            "album_list.html",
            {
                "favourite_album": favourite_album,
                "comments": comments,
            },
        )



def post_view(request, slug, *args, **kwargs):
   
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved = True).count()
    liked = False
    commented = False

    if post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment awaiting moderation.')
        else:
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "post_view.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "liked": liked,
            "comment_form": comment_form
        },
    )


def post_like(request, slug, *args, **kwargs):

    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST" and request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_view', args=[slug]))


def comment_edit(request, slug, comment_id, *args, **kwargs):

    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = post.comments.filter(id=comment_id).first()

        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.name == request.user.username:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_view', args=[slug]))


def comment_delete(request, slug, comment_id, *args, **kwargs):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset)
    comment = post.comments.filter(id=comment_id).first()

    if comment.name == request.user.username:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_view', args=[slug]))