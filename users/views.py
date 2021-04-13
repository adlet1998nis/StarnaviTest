from rest_framework import decorators, viewsets, permissions
from rest_framework.response import Response

from . import serializers, models


class RegisterViewSet(viewsets.ViewSet):

    @decorators.action(detail=False, methods=['POST'])
    def signup(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserInfoViewSet(viewsets.ViewSet):

    permission_classes = (permissions.IsAuthenticated,)

    @decorators.action(detail=False)
    def activity(self, request):
        user = models.User.objects.get(id=request.user.id)
        return Response({
            'last_login': user.last_login,
            'last_request': user.last_request,
        })
