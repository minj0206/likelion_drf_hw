from django.shortcuts import render

# Create your views here.
# project > Sing > views.py > Sing_list_create

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Singer, Song
from .serializers import SingerSerializer, SongSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def singer_list_create(request):
    if request.method == 'GET':
        Singers = Singer.objects.all()
        serializer = SingerSerializer(Singers, many=True)
        return Response(data=serializer.data)

    if request.method == 'POST':
        serializer = SingerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

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
