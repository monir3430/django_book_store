from django.shortcuts import render
from book_store.forms import bookForm


# Create your views here.
def home(request):
    return render(request, 'store.html')


def store(request):
    book = bookForm(request.POST)
    print(book)
    return render(request, 'store.html', {'form': book})
