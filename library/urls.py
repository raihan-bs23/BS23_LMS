from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('view_all_book/', views.all_books, name='all_books'),
    path('add/book/',views.add_book,name='add_book'),
    path('add/category/',views.add_category,name='add_category'),
    path('book_added/', views.book_added, name='book_added'),
    path('item/<slug:slug>/', views.book_detail, name='book_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    path('add/copy/', views.add_copy_form, name='add_copy'),
    path('owned/copy/', views.owned_copy, name='owned_books'),
    path('borrowed/copy/', views.borrowed_copy, name='borrowed_books'),
    path('borrow/<slug:slug>/', views.borrow_copy, name='borrow_copy'),
    path('searchbooks/', views.search_books, name='search_books'),

]
