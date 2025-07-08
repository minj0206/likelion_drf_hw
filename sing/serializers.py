from rest_framework import serializers
from .models import Singer, Song

class SongSerializer(serializers.ModelSerializer):
    singer = serializers.SlugRelatedField(
        queryset=Singer.objects.all(),
        slug_field='name' 
    )

    class Meta:
        model = Song
        fields = '__all__'


class SingerSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Singer
        fields = '__all__'
