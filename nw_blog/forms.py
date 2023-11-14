from .models import Comment, FavouriteAlbum
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class FavouriteAlbumForm(forms.ModelForm):
    
    class Meta:
        model = FavouriteAlbum
        fields = ['fav_album']
        widgets = {
            'fav_album': forms.Select()
        }