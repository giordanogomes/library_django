from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("book.urls")),
    path("auth/", include("user.urls")),
    path("captcha/", include("captcha.urls"))
]
