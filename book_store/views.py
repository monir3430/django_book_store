from django.shortcuts import render, redirect
from book_store.forms import bookForm
from book_store.models import bookModel


# Create your views here.
def home(request):
    return render(request, 'store.html')


def store(request):
    if request.method == 'POST':
        book = bookForm(request.POST)
        if book.is_valid():
            book.save()
            return redirect('show_book')
    else:
        book = bookForm()
    return render(request, 'store.html', {'form': book})


def show_book(request):
    book = bookModel.objects.all()
    return render(request, 'show.html', {"data": book})


def edit_book(request, id):
    book = bookModel.objects.get(pk=id)
    form = bookForm(instance=book)
    if request.method == 'POST':
        form = bookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show_book')
    return render(request, 'store.html', {'form': form})


def delete_book(request, id):
    book = bookModel.objects.get(pk=id)
    book.delete()
    return redirect('show_book')
    return render(request, 'store.html', {'form': form})
