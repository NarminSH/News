from django.db import models
from django.urls.base import reverse_lazy
from users.models import User


# Create your models here.


class Post(models.Model):

    """
    This model saves all posts
    """

    # information
    author_name = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True, related_name="posts"
    )
    upvote_amount = models.ManyToManyField(User, related_name="upvotes", blank=True)
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=140, null=True, blank=True)
    content = models.TextField(max_length=500)

    # moderations
    creation_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse_lazy("single-post", kwargs={"link": self.link})

    def __str__(self):
        return self.title


class Comment(models.Model):

    """
    This model shows comments for particular post
    """

    # relations
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, db_index=True, related_name="comments"
    )

    # information
    author_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        related_name="comments",
    )
    content = models.TextField(max_length=500)

    # moderations
    creation_date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.content
