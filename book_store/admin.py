from django.contrib import admin
from book_store.models import bookModel


# Register your models here.
class bookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'author', 'category', 'price', 'first_publish', 'last_publish')


admin.site.register(bookModel, bookAdmin)
