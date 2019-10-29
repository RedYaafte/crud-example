from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializers


@api_view(['GET', 'POST'])
def note_list(request):
    if request.method == 'GET':
        note = Note.objects.all()
        serializer = NoteSerializers(note, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NoteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def note_detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = NoteSerializers(note)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = NoteSerializers(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method =='DELETE':
        note.delete()
        return Response(status=204)