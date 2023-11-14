from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('concert_memories/', views.ConcertMemoriesView.as_view(), name='concert_memories'),
    path('favourite_album/', views.FavouriteAlbumView, name='favourite_album'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_view'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like')
]
