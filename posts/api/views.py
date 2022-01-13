from django.http.response import JsonResponse
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from posts.api.serializers import (
    CommentListSerializer,
    CommentSerializer,
    PostSerializer,
)
from posts.models import Comment, Post


class PostsAPIView(ListCreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = "pk"

    def put(self, *args, **kwargs):
        post_data = self.request.data
        post = Post.objects.filter(id=kwargs.get("pk")).first()
        if self.request.user == post.author_name:
            serializer = PostSerializer(
                data=post_data, context={"request": self.request}
            )
            serializer.is_valid(raise_exception=True)
            serializer.validated_data["author_name"] = self.request.user
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status=201)
        return JsonResponse(
            data="You do not have permissions to make changes to others' posts!",
            status=403,
            safe=False,
        )

    def delete(self, *args, **kwargs):
        post = Post.objects.filter(id=kwargs.get("pk")).first()
        if self.request.user == post.author_name:
            post.delete()
            return JsonResponse(
                {"message": "The post was deleted successfully!"}, status=200
            )
        return JsonResponse(
            data="You do not have permissions to delete to others' posts!",
            status=403,
            safe=False,
        )


class CommentsAPIView(ListCreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CommentSerializer
        return super(CommentsAPIView, self).get_serializer_class()


class CommentAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = "pk"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentListSerializer
        return super(CommentAPIView, self).get_serializer_class()

    def put(self, *args, **kwargs):
        comment_data = self.request.data
        comment = Comment.objects.filter(id=kwargs.get("pk")).first()
        if self.request.user == comment.author_name:
            serializer = CommentSerializer(comment, data=comment_data)
            serializer.is_valid(raise_exception=True)
            serializer.save(author_name=self.request.user)
            return JsonResponse(data=serializer.data, safe=False, status=201)
        return JsonResponse(
            data="You do not have permissions to make changes to others' comments!",
            status=403,
            safe=False,
        )

    def delete(self, *args, **kwargs):
        comment = Comment.objects.filter(id=kwargs.get("pk")).first()
        if self.request.user == comment.author_name:
            comment.delete()
            return JsonResponse(
                {"message": "The comment was deleted successfully!"}, status=200
            )
        return JsonResponse(
            data="You do not have permissions to delete others' comments!",
            status=403,
            safe=False,
        )


class PostCommentsAPIView(ListAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all()

    def get(self, *args, **kwargs):
        comment = Comment.objects.filter(post=kwargs.get("pk"))
        if not comment:
            return JsonResponse(data=[], status=200, safe=False)
        serializer = CommentListSerializer(
            comment, many=True, context={"request": self.request}
        )
        return JsonResponse(data=serializer.data, safe=False)


class UpvoteAPIView(UpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = "pk"

    def patch(self, request, *args, **kwargs):
        post = Post.objects.filter(id=kwargs.get("pk")).first()
        if post.upvote_amount.filter(id=self.request.user.id).exists():
            return JsonResponse({"message": "You already upvoted"}, status=200)
        post.upvote_amount.add(self.request.user)
        return self.partial_update(request, *args, **kwargs)

    def reset_upvote(self):
        posts = Post.objects.all()
        for post in posts:
            if post.upvote_amount.count() > 0:
                post.upvote_amount.clear()
                print(post.upvote_amount.count())
