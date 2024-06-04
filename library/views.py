# from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Lib



def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        publishing = request.POST.get('publisher')
        genre = request.POST.get('genre')
        year = request.POST.get('year')
        picture = request.POST.get('cover')
        new_book = Lib(name=name, author=author, 
                       publishing=publishing, genre=genre, 
                       year=year, picture=picture)
        new_book.save()

    books = Lib.objects.all()
    return render(request, 'index.html',{"books":books})


def bookcard(request,id):
    book = Lib.objects.get(pk=id)
    if request.method == 'POST':
        option = request.POST.get('option')
        if option == "edit":
            book.name = request.POST.get('name')
            book.author = request.POST.get('author')
            book.publishing = request.POST.get('publisher')
            book.genre = request.POST.get('genre')
            book.year = request.POST.get('year')
            book.picture = request.POST.get('cover')
            book.review = request.POST.get('review')
            book.rate = request.POST.get('rate')
        else:
            if "add" in request.POST:
                book.read = True
                book.review = request.POST.get('review')
                book.rate = request.POST.get('rate')
            else:
                book.read = False
                book.review = None
                book.rate = None
        book.save()

    return render(request, 'bookcard.html', {"book":book})

from django.db.models import Q
def search(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        publishing = request.POST.get('publisher')
        genre = request.POST.get('genre')
        year = request.POST.get('year')
        picture = request.POST.get('cover')
        new_book = Lib(name=name, author=author, 
                       publishing=publishing, genre=genre, 
                       year=year, picture=picture)
        new_book.save()
    genre = request.GET.get('filter')
    query = request.GET.get('search')
    if genre == "Все":
        books = Lib.objects.filter(Q(name__icontains=query) | Q(name__icontains=query.capitalize()))
    else:
        books = Lib.objects.filter(Q(name__icontains=query) | Q(name__icontains=query.capitalize()), genre__contains=genre)
    return render(request, 'index.html',{"books":books})

def readcard(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        publishing = request.POST.get('publisher')
        genre = request.POST.get('genre')
        year = request.POST.get('year')
        picture = request.POST.get('cover')
        # read = request.POST.get('read')
        new_book = Lib(name=name, author=author, 
                       publishing=publishing, genre=genre, 
                       year=year, picture=picture)
        new_book.save()
    books = Lib.objects.filter(read = True)
    return render(request, 'index.html',{"books":books})

def delete(request, id):
    Lib.objects.filter(pk=id).delete()
    return HttpResponseRedirect("/")

    

# class BookListView(generic.ListView):
#     model = Lib