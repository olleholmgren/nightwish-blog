from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_view'),
    path('favourite_album/', views.FavouriteAlbumView.as_view(), name='favourite_album'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like')
]
