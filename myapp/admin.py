from django.contrib import admin

# Register your models here.
from easy_select2 import select2_modelform

from myapp.models import Book, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


BookForm = select2_modelform(Book, attrs={'width': '250px'})


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    form = BookForm
