import uuid

from django.db import models


class Post(models.Model):
    post_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    author = models.ForeignKey('users.SocialUser', on_delete=models.CASCADE)
    title = models.CharField('Post title', max_length=255)
    post_content = models.TextField('Post content')
    pub_date = models.DateTimeField('Published', auto_now_add=True)


class Like(models.Model):
    post_id = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    user_of_like = models.ForeignKey(
        'users.SocialUser', on_delete=models.CASCADE,
    )
