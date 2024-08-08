# admin.py
from django.contrib import admin
from .models import Book, CustomBookData

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'is_featured')  # Ensure these fields exist in the model
    search_fields = ('title', 'author')
    list_filter = ('publication_date', 'is_featured')
    ordering = ('-publication_date',)  # Use fields defined in the Book model
    fields = ('title', 'author', 'description', 'cover_image', 'publication_date', 'is_featured')

@admin.register(CustomBookData)
class CustomBookDataAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Ensure these fields exist in the model
    search_fields = ('field1', 'field2')
    ordering = ('field1',)  # Ensure field1 exists
