from django.test import TestCase
from .forms import FavouriteAlbumForm


class TestFavouriteAlbumForm(TestCase):
    """
    This function tests if the body
    field is required.
    """

    def test_comment_body_is_required(self):
        form = FavouriteAlbumForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')