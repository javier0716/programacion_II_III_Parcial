from django.db import models
from uuid import uuid4

# Create your models here.

class Author(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, blank=False, default=uuid4)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False)
    born_date = models.DateField(blank=False)
    died_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=False)
    is_deleted = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, blank=False, default=uuid4)
    title = models.CharField(max_length=100, blank=False)
    release_date = models.DateField(blank=False)
    isbn = models.CharField(max_length=50, unique=True, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title



