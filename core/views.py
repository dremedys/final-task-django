from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from core.models import *
from core.serializers import *


class BooksView(APIView):

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializers = BookSerializer(books, many=True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JournalViewSet(viewsets.ModelViewSet):
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterViewSet(ViewSet):
    @action (detail=False, methods=['POST'])
    def register(self, request):
        serializer = serializers.UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)