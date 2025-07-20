from django.shortcuts import render
from book_outlet.models import Book

# Create your views here.

def bookList(request):
    books = Book.objects.all()
    return render(request, 'book_outlet/booklist.html', {'books':books})

def bookDetailsById(request, id):
    book = Book.objects.get(id=id)
    

def bookDetails(request, slug):
    book = Book.objects.get(slug = slug)
    return render(request, 'book_outlet/bookdetails.html', {'title': book.title, "rating": book.rating, "author":book.author})