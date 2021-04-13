from rest_framework import decorators, mixins, viewsets, permissions
from rest_framework.response import Response

from . import filters, models, serializers


class PostViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    ACTION_SERIALIZERS = {
        'create': serializers.PostCreateSerializer,
        'like': serializers.PostLikeSerializer,
        'unlike': serializers.PostUnlikeSerializer,
    }

    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Post.objects.all()

    def get_serializer_class(self):
        if self.action in self.ACTION_SERIALIZERS:
            return self.ACTION_SERIALIZERS[self.action]

        return super().get_serializer_class()

    def perform_create(self, serializer):
        user = serializer.context['request'].user
        serializer.save(user=user)

    @decorators.action(detail=True, methods=['PATCH'])
    def like(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @decorators.action(detail=True, methods=['PATCH'])
    def unlike(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class AnalyticsViewSet(viewsets.GenericViewSet):

    queryset = models.Like.objects.all()
    filterset_class = filters.AnalyticsFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return Response({'count': queryset.count()})
