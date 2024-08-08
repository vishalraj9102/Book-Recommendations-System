from rest_framework import serializers
from .models import Book, Recommendation, CustomBookData

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'
        

class CustomBookDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomBookData
        fields = '__all__'

