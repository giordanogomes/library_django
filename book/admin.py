from django.contrib import admin

from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display =  ('id', 'name', 'author', 'registration_date')
    list_display_links = ("id", "name")

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
