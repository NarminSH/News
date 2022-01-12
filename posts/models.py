from django.db import models
from django.urls.base import reverse_lazy


# Create your models here.


class Post(models.Model):

    """
    This model saves all posts
    """


    # information
    author_name = models.CharField(verbose_name="Author", max_length=50)
    upvote_amount = models.IntegerField(default=0)
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
        Post,
        on_delete=models.CASCADE,
        db_index=True,
        related_name="comments",
        null=True,
        blank=True,
    )

    # information
    author_name = models.CharField(verbose_name="Author", max_length=50)
    content = models.TextField(max_length=500)

    # moderations
    creation_date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.author_name
