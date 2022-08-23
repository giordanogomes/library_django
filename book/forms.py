from django import forms

from .models import Book, Category, Borrowing


class RegisterBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        # ("name", "author", "co_author", "registration_date", "category")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].widget = forms.HiddenInput()


class RegisterCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].widget = forms.HiddenInput()
        
        
class RegisterBorrowing(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = "__all__"
