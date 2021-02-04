from django.urls import path
from posts.views import FeedView
from posts.views import CreatePostApiView, LikePostApiView, UnlikePostApiView

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    # Create post by API
    path(
        'posts/api/create_post',
        CreatePostApiView.as_view(),
        name='create_post',
    ),

    # Like post by API
    path(
        'posts/api/like_post',
        LikePostApiView.as_view(),
        name='like_post',
    ),

    # Unlike post by API
    path(
        'posts/api/unlinke_post',
        UnlikePostApiView.as_view(),
        name='unlike_post',
    ),
]
