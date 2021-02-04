from rest_framework.generics import CreateAPIView, UpdateAPIView
from django.views.generic import ListView
from posts.models import Post


class FeedView(ListView):
    model = Post
    template_name = 'posts/feed.html'


class CreatePostApiView(CreateAPIView):
    pass


class LikePostApiView(UpdateAPIView):
    pass


class UnlikePostApiView(UpdateAPIView):
    pass
