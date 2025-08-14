from django.urls import path
from .views import *

urlpatterns = [
    path('book/list', ListBooks.as_view(), name="list_all_books"),
    path('book/add', BookAdd.as_view(), name="add_book"),
    path('book/<uuid:book_id>/detail', BookDetail.as_view(), name="book_detail"),
    path('book/<uuid:book_id>/delete', BookDelete.as_view(), name="book_delete"),
    path('author/list', ListAuthors.as_view(), name="list_authors"),
    path('author/add', AuthorAdd.as_view(), name="add_author"),
    path('book/<uuid:author_id>/detail', AuthorDelete.as_view(), name="author_delete"),
    
    
]