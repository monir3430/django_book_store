from django import forms
from book_store.models import bookModel


class bookForm(forms.ModelForm):
    class Meta:
        model = bookModel
        exclude = ['first_publish', 'last_publish']
