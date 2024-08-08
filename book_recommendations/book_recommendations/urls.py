from django.contrib import admin
from django.urls import path, include
from books.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    path('', home, name='home'),
]
