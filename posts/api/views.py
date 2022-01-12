from django.http.response import JsonResponse
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
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = "pk"


class CommentsAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CommentSerializer
        return super(CommentsAPIView, self).get_serializer_class()


class CommentAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = "pk"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentListSerializer
        return super(CommentAPIView, self).get_serializer_class()


class PostCommentsAPIView(ListAPIView):
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
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = "pk"

    def patch(self, request, *args, **kwargs):
        post = Post.objects.filter(id=kwargs.get("pk")).first()
        post.upvote_amount += 1
        post.save()
        return self.partial_update(request, *args, **kwargs)
