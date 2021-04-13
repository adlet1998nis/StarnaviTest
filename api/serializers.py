from rest_framework import serializers

from .models import Post


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'text')


class PostLikeSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'likes_count')

    def update(self, instance, validated_data):
        instance.likes.create(user=self.context['request'].user)
        return instance

    def get_likes_count(self, instance):
        return instance.likes.count()


class PostUnlikeSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'likes_count')

    def update(self, instance, validated_data):
        likes = instance.likes.filter(user=self.context['request'].user)
        if likes.exists():
            last_like = likes.order_by('created').last()
            last_like.delete()

        return instance

    def get_likes_count(self, instance):
        return instance.likes.count()
