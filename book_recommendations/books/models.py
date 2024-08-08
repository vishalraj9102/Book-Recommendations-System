from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)  # Updated field name

    def __str__(self):
        return self.title

class Recommendation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

class CustomBookData(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Updated reference
    additional_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
