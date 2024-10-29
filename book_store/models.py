from django.db import models


# Create your models here.
class bookModel(models.Model):
    type = (
        ('Mystery', 'Mystery'),
        ('Thriller', 'Thriller'),
        ('Flying', 'Flying'),
        ('Horror', 'Horror'),
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=type)
    first_publish = models.DateTimeField(auto_now_add=True)
    last_publish = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

