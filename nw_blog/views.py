from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
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
    success_url = reverse_lazy('user_favourite_albums')

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Your favourite album has been saved')
        return response


@login_required
def FavouriteAlbum_delete(request, favouritealbum_id):
    album = get_object_or_404(FavouriteAlbum, id=favouritealbum_id, author=request.user)
    album.delete()
    messages.success(request, 'Your favorite album has been deleted.')
    return redirect('favourite_album_deleted')


@login_required
def FavouriteAlbum_edit(request, favouritealbum_id):
    album = get_object_or_404(FavouriteAlbum, id=favouritealbum_id, author=request.user)
    if request.method == 'POST':
        form = FavouriteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your favorite album has been updated.')
            return redirect('favourite_album_edited')
    else:
        form = FavouriteAlbumForm(instance=album)
    return render(request, 'favourite_album_edit.html', {'form': form})


class AlbumListView(generic.ListView):

    model = FavouriteAlbum
    template_name = 'album_list.html'
    paginate_by = 8

    def get_queryset(self):
        return FavouriteAlbum.objects.filter(author=self.request.user, status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favourite_album_form'] = FavouriteAlbumForm(self.request.POST or None)

        if self.request.POST:
            context['selected_album'] = self.request.POST.get('favourite_album', None)
        return context

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return self.render_to_response(self.get_context_data())


class FavouriteAlbumEdited(generic.ListView):

    model = FavouriteAlbum
    template_name = 'favourite_album_edited.html'

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return self.render_to_response(self.get_context_data())


class FavouriteAlbumDeleted(generic.ListView):

    model = FavouriteAlbum
    template_name = 'favourite_album_deleted.html'


class UserFavouriteAlbumListView(generic.ListView):

    model = FavouriteAlbum
    template_name = 'user_favourite_albums.html'
    context_object_name = 'favourite_albums'


def post_view(request, slug, *args, **kwargs):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
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
