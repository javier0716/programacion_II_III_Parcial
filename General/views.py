from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django import views
from django.http import HttpRequest
from .models import *
from uuid import UUID
from .forms import *

# Create your views here.

class ListBooks(views.View):
    def get(self, request:HttpRequest):
        books = Book.objects.filter(is_deleted=False)
        return render(request, 'book_list.html', {"books": books})


class BookAdd(views.View):
    def get(self, request:HttpRequest):
        form = BookForm()
        return render(request, 'book_form.html', {'form': form})
    

    def post(self, request:HttpRequest):
        form = BookForm(request.POST)
        if not form.is_valid():
            return render (request, 'book_form.html', {'form': form})

        book = Book()
        book.title = form.cleaned_data['title']
        book.release_date = form.cleaned_data['release_date']
        book.isbn= form.cleaned_data['isbn']
        book.author= form.cleaned_data['author'] 
        book.save()             
        
        return HttpResponseRedirect(reverse('list_all_books'))

class BookDetail(views.View):
    def get(self, request:HttpRequest, book_id:UUID):
        # book = Book.objects.get(id=book_id)
        book = Book.objects.filter(id=book_id).first()

        if book is None:
            return render(request, '404.html', status=404)

        return render(request, 'book_detail.html', {'book': book})

class BookDelete(views.View):
    def delete(self, request:HttpRequest, book_id:UUID):
       book = Book.objects.filter(id=book_id).first()

       if book is None:
            return render(request, '404.html', status=404) 
       
       book.is_deleted = True
       book.save()

       return HttpResponseRedirect(reverse('list_all_books'))
    
class ListAuthors(views.View):
    def get(self, request:HttpRequest):
        authors = Author.objects.all()
        return render(request, 'author_list.html', {'authors': authors})
    

class AuthorAdd(views.View):
    def get(self, request:HttpRequest):
        form = AuthorForm()
        
        return render(request, 'author_form.html', {'form': form})
    
    def post(self, request:HttpRequest):
        form = AuthorForm(request.POST)
        if not form.is_valid():
            return render (request, 'author_form.html', {'form': form})

        author = Author()
        author.name = form.cleaned_data['name']
        author.email = form.cleaned_data['email']
        author.born_date=form.cleaned_data['born_date']
        author.died_date= form.cleaned_data['died_date']
        author.country = form.cleaned_data['country']   
        author.save()
        
        return HttpResponseRedirect(reverse('list_authors'))
    
class AuthorDelete(views.View):
    def post(self, request:HttpRequest, author_id:UUID):
       author = Author.objects.filter(id=author_id).first()

       if author is None:
            return render(request, '404.html', status=404) 
       
       author.is_deleted = True
       author.save()

       return HttpResponseRedirect(reverse('list_authors'))
    