from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('library:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, related_name='book', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    publisher = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    in_stock = models.BooleanField(default=False)
    edition = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Books'

    def get_absolute_url(self):
        return reverse('library:book_detail', args=[self.slug])

    def __str__(self):
        return self.title


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)

    def __str__(self):
        return self.content


class Copy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')
    copy = models.IntegerField(verbose_name='Copies')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner', default=1)
    STATUS = [
        ('available', 'available'),
        ('borrowed', 'borrowed'), ]
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return f'{self.book.title}(copy-{self.copy}, {self.status})'


class Borrow(models.Model):
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE, related_name='borrow')
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='borrow')
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def return_book(self):
        self.return_date = timezone.now

    def __str__(self):
        return f'{self.copy.book} borrowed by {self.borrower}'