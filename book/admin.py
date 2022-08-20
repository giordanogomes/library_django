from django.contrib import admin

from .models import Book, Category, Borrowing


class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author", "category", "registration_date")
    list_display_links = ("id", "name")


class BorrowingAdmin(admin.ModelAdmin):
    list_display = ("name_borrowed", "name_borrowed_anonymous", "book")


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Borrowing, BorrowingAdmin)
