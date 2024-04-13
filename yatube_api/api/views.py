from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import (BasePermission,
                                        IsAuthenticated,
                                        SAFE_METHODS
                                        )
from rest_framework import viewsets

from posts.models import Group, Post
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_post_id(self):
        post_id = self.kwargs.get('post_id')
        if Post.objects.get(pk=post_id):
            return post_id
        return ObjectDoesNotExist('Отсутствует пост'
                                  f'с таким post_id: {post_id}!')

    def perform_create(self, serializer):
        post_id = self.get_post_id()
        serializer.save(author=self.request.user, post_id=post_id)

    def get_queryset(self):
        post_id = self.get_post_id()
        new_queryset = Post.objects.get(pk=post_id).comments.all()
        return new_queryset
