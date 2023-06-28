from .models import Comment, FavouriteAlbum
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class FavouriteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['review'].widget.attrs.update({'class': 'review-box', 'placeholder': 'Type your review here...'})

    class Meta:
        model = FavouriteAlbum
        fields = ('album_title', 'review',)