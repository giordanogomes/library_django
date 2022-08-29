from django.contrib import admin

from .models import Book, Category, Borrowing


class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author", "category", "registration_date", "user")
    list_display_links = ("id", "name")


class BorrowingAdmin(admin.ModelAdmin):
    list_display = ("username", "book")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "user")


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Borrowing, BorrowingAdmin)
