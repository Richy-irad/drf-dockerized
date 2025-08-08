from django.db import models

# Create your models here.
class Book(models.Model):
    """Book model to represent a book.

    Args:
        models (Model): _description_

    Returns:
        _type_: _description_
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    
    def __str__(self):
        return self.title
