from django.shortcuts import render

# Create your views here.
# project > Sing > views.py > Sing_list_create

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Singer, Song, Tag, Comment
from .serializers import SingerSerializer, SongSerializer, CommentSerializer, TagSerializer


def test():
    pass

@api_view(['GET', 'POST'])
def singer_list_create(request):
    if request.method == 'GET':
        singers = Singer.objects.all()
        serializer = SingerSerializer(singers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SingerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            singer = serializer.save()
            content = request.data.get('content', '')
            tags = [word[1:] for word in content.split() if word.startswith('#')]
            for t in tags:
                tag, _ = Tag.objects.get_or_create(name=t)
                singer.tags.add(tag)
            return Response(SingerSerializer(singer).data)

@api_view(['GET', 'PATCH', 'DELETE'])
def sing_detail_update_delete(request, sing_id):
    singer = get_object_or_404(Singer, id=sing_id)

    if request.method == 'GET':
        serializer = SingerSerializer(singer)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = SingerSerializer(instance=singer, data=request.data, partial=True)
        if serializer.is_valid():
            singer = serializer.save()
            singer.tags.clear()
            content = request.data.get('content', '')
            tags = [word[1:] for word in content.split() if word.startswith('#')]
            for t in tags:
                tag, _ = Tag.objects.get_or_create(name=t)
                singer.tags.add(tag)
            return Response(SingerSerializer(singer).data)

    elif request.method == 'DELETE':
        singer.delete()
        return Response({'deleted_singer': sing_id})

@api_view(['GET', 'POST'])
def song_list_create(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])
def comment_read_create(request, sing_id):
    singer = get_object_or_404(Singer, id=sing_id)

    if request.method == 'GET':
        comments = Comment.objects.filter(singer=singer)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(singer=singer)
        return Response(serializer.data)

@api_view(['GET'])
def find_tag(request, tags_name):
    tag = get_object_or_404(Tag, name=tags_name)
    singers = Singer.objects.filter(tags__in=[tag])
    serializer = SingerSerializer(singers, many=True)
    return Response(serializer.data)
