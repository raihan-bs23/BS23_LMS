# forms.py
from django import forms
from .models import Book, Category, Copy


class BookForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = ['category', 'title', 'author', 'description', 'image', 'publisher', 'slug', 'edition']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class CopyForm(forms.ModelForm):
    class Meta:
        model = Copy
        fields = ['book', 'copy']
