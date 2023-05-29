from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator

def books_view(request):
    template = 'books/books_list.html'
    books_objects = Book.objects.all()
    context = {'books':books_objects}
    return render(request, template, context)

def books_date(request,pubdate):
    template = 'books/books_index.html'
    content_list = []
    content_list.append(Book.objects.get(pub_date=pubdate))
    for item in Book.objects.all().order_by('pub_date')[1:]:
        content_list.append(item)
    paginator = Paginator(content_list,1)
    page_date = int(request.GET.get('page',1))
    page = paginator.get_page(page_date)
    context = {'books':page,'page':page}
    
    return render(request, template, context)