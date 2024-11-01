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
    last_publish = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.book_name


class common(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)

    class meta:
        abstract = True


class author(common):
    address = models.CharField(max_length=100)


class reader(common):
    likes = models.CharField(max_length=30)
    dislikes = models.CharField(max_length=30)


class people(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


class man(people):
    power = models.BooleanField()
    monogamy = models.BooleanField()


class women(people):
    married = models.BooleanField()
    unmarried = models.BooleanField()
