from django.db import models


# Create your models here.
from django.db.models import CASCADE


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.first_name, self.description)


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.publisher_name, self.description)


class Book(models.Model):
    book_name = models.CharField(max_length=30)
    book_series_name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.OneToOneField(
        Publisher,
        primary_key=True,
        on_delete=models.CASCADE
    )
    isbn = models.BigIntegerField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s %s %s %d %s" % (
            self.book_name, self.book_series_name, self.author, self.publisher, self.isbn, self.description)
