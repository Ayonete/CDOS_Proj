"""
this module represents the book table for this application which we need for
several functions across the application that are related to data such as CRUD functions
"""
from django.db import models

# Create your models here.
# the Book model with its fields
# pylint: disable=too-few-public-methods
class Book(models.Model):
    """ this class defines books model"""
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    review = models.TextField(default="nothing to say", max_length=500)
    rating = models.IntegerField(default="5")
    # this is the image for a book, the image will be uploaded to images folder
    image = models.ImageField(null=False, blank=False, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    # this is the string representation
    # what to display after querying a book/books
    def __str__(self):
        return f'{self.title}'

    # this will order the books by date created
    class Meta:
        ordering = ['-created_at']
