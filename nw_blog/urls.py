from django.contrib import admin
from django.urls import path, include
from .views import IndexView, PostDetailView, FavouriteAlbumView, PostLike

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_view'),
    path('favourite_album/', FavouriteAlbumView.as_view(), name='favourite_album'),
    path('like/<slug:slug>', PostLike.as_view(), name='post_like')
]
