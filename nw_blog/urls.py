from django.contrib import admin
from django.urls import path, include
from .views import IndexView, PostDetailView, FavouriteAlbumView, PostLike

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_view'),
    path('favourite_album/', FavouriteAlbumView.as_view(), name='favourite_album'),
    path('like/<slug:slug>', PostLike.as_view(), name='post_like')
]
