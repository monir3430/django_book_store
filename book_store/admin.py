from django.contrib import admin
from book_store.models import bookModel, author, reader, people, man, women


# Register your models here.
class bookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'author', 'category', 'price', 'first_publish', 'last_publish')


admin.site.register(bookModel, bookAdmin)
admin.site.register(author)
admin.site.register(reader)


# Register People model with the admin site
@admin.register(people)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')  # Fields to display in the list view
    search_fields = ('name',)  # Enable search by 'name'


# Register Man model with the admin site
@admin.register(man)
class ManAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'power', 'monogamy')  # Include inherited and unique fields
    list_filter = ('power', 'monogamy')  # Add filters for 'power' and 'monogamy'


# Register Women model with the admin site
@admin.register(women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'married', 'unmarried')  # Include inherited and unique fields
    list_filter = ('married', 'unmarried')  # Add filters for 'married' and 'unmarried'
