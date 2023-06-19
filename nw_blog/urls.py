from django.urls import path
from .views import IndexView, PostDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    #path('post_view/', PostDetailView.as_view(), name='post_view'),
    path('post_view/<int:pk>', PostDetailView.as_view(), name='post_view')
]

