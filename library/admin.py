from django.contrib import admin

# Register your models here.
from .models import *

# @admin.register(Book)
# class Bookadmin(admin.ModelAdmin):
#     list_display = ['id']
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Copy)
admin.site.register(Borrow)