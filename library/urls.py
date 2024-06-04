from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bookcard/<int:id>', views.bookcard, name="bookcard"),
    path('readcard', views.readcard, name="readcard"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('search', views.search, name='search'),
    # path('search', views.search, name="search"),
    #path('addbook', views.addbook, name='index'),
    # path('books/', views.BookListView.as_view(), name='books'),
    # urls(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail')
]

