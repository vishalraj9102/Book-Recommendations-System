# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, RecommendationViewSet, CustomBookDataViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'recommendations', RecommendationViewSet)
router.register(r'custom-book-data', CustomBookDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
