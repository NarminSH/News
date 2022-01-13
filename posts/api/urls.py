from django.urls import path
from posts.api.views import (
    CommentsAPIView,
    PostCommentsAPIView,
    PostsAPIView,
    PostAPIView,
    CommentAPIView,
    UpvoteAPIView,
)

app_name = "posts_api"

urlpatterns = [
    path("posts/", PostsAPIView.as_view(), name="posts"),
    path("posts/<int:pk>", PostAPIView.as_view(), name="post"),
    path(
        "posts/<int:pk>/comments", PostCommentsAPIView.as_view(), name="post-comments"
    ),
    path("posts/<int:pk>/upvote", UpvoteAPIView.as_view(), name="upvote-comment"),
    path("comments/", CommentsAPIView.as_view(), name="comments"),
    path("comments/<int:pk>", CommentAPIView.as_view(), name="comment"),
]
