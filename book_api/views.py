from django.shortcuts import render
from book_api.models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from book_api.serializers import BookSerializer

# Create your views here.
@api_view(['GET'])
def book_list(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def book(request,pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return serializer.errors
    if request.method == 'DELETE':
        book.delete()
        return Response('Item deleted')
    