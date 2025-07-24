from django.urls import path
from .views import *

urlpatterns = [
    path('book/list', ListBooks.as_view(), name="list_all_books"),
    path('book/add', BookAdd.as_view(), name="add_book"),
    path('book/<uuid:book_id>/detail', BookDetail.as_view(), name="book_detail"),
    path('author/list', ListAuthors.as_view(), name="list_authors"),
    path('author/add', AuthorAdd.as_view(), name="add_author")
    
    
]