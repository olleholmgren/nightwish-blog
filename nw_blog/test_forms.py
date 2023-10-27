from django.test import TestCase
from .forms import CommentForm

class TestCommentForm(TestCase):

    def test_comment_form_name_is_required(self):
        form = CommentForm({'name': ''}))

