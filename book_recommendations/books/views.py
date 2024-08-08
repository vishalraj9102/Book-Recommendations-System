# views.py
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Book, Recommendation
from .serializers import BookSerializer, RecommendationSerializer, CustomBookDataSerializer, CustomBookData
import requests

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
        response = requests.get(url)
        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response({'error': 'Unable to fetch data from Google Books API'}, status=response.status_code)

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_books = Book.objects.filter(featured=True)[:10]
        serializer = BookSerializer(featured_books, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def detail(self, request, pk=None):
        url = f'https://www.googleapis.com/books/v1/volumes/{pk}'
        response = requests.get(url)
        if response.status_code == 200:
            book_data = response.json()
            return Response(book_data)
        else:
            return Response({'error': 'Book not found'}, status=404)

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        recommendation = self.get_object()
        recommendation.likes += 1
        recommendation.save()
        return Response({'status': 'Recommendation liked'})

class CustomBookDataViewSet(viewsets.ModelViewSet):
    queryset = CustomBookData.objects.all()
    serializer_class = CustomBookDataSerializer


def home(request):
    return render(request, 'index.html')
