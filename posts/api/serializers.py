from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):  # serializer for all methods
    class Meta:
        model = Post
        fields = (
            "id",
            "author_name",
            "upvote_amount",
            "title",
            "link",
            "content",
            "creation_date",
        )


class CommentSerializer(
    serializers.ModelSerializer
):  # serializer for put, patch and delete method
    class Meta:
        model = Post
        fields = (
            "id",
            "post",
            "author_name",
            "content",
            "creation_date",
        )


class CommentListSerializer(CommentSerializer):  # serializer for get method
    post = PostSerializer()
