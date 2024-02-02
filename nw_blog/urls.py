from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('concert_memories/', views.ConcertMemoriesView.as_view(), name='concert_memories'),
    path('favourite_album/', views.FavouriteAlbumView.as_view(), name='favourite_album'),
    path('album_list/', views.AlbumListView.as_view(), name='album_list'),
    path('user_favourite_albums/', views.UserFavouriteAlbumListView.as_view(), name='user_favourite_albums'),
    path('<slug:slug>/', views.post_view, name='post_view'),
    path('like/<slug:slug>', views.post_like, name='post_like'),
    path('delete_body/<int:favouritealbum_id>/', views.FavouriteAlbum_delete, name='favouritealbum_delete'),
    path('edit_body/<int:favouritealbum_id>/', views.FavouriteAlbum_edit, name='favouritealbum_edit')
]
