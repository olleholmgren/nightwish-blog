from django.urls import path
from .views import IndexView, PostDetailView, FavouriteAlbumView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    #path('post_view/', PostDetailView.as_view(), name='post_view'),
    path('post_view/<int:pk>', PostDetailView.as_view(), name='post_view'),
    path('favourite_album/', FavouriteAlbumView.as_view(), name='favourite_album'),
]

