from .models import Comment, FavouriteAlbum
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class FavouriteAlbumForm(forms.ModelForm):

    class Meta:
        model = FavouriteAlbum
        fields = ('favourite_album', 'body')
        widgets = {
            'favourite_album': forms.Select(),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(FavouriteAlbumForm, self).__init__(*args, **kwargs)
        self.fields['favourite_album'].label = "Please select an album from this list"
        self.fields['body'].label = "Why is this your favourite album?"
