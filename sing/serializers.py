from rest_framework import serializers
from .models import Singer, Song, Tag, Comment

class SongSerializer(serializers.ModelSerializer):
    singer = serializers.SlugRelatedField(
        queryset=Singer.objects.all(),
        slug_field='name' 
    )

    class Meta:
        model = Song
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
        read_only_fields=['movie']


class SingerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    songs = SongSerializer(many=True, read_only=True)

    comments = serializers.SerializerMethodField(read_only=True)


    def get_comments(self, instance):
        serializer = CommentSerializer(instance.comments, many=True)
        return serializer.data

    tags = serializers.SerializerMethodField()

    def get_tags(self, instance):
        tag = instance.tags.all()
        return [t.name for t in tag]

    class Meta:
        model = Singer
        fields = '__all__'

    image =serializers.ImageField(use_url=True, required=False)

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'
