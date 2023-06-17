from django.db import models
from django.urls import reverse_lazy

class Author(models.Model):
    name = models.CharField(
        verbose_name='Author of books',
        max_length=30
    )

    def __str__(self):
        return self.name
    
class Publish(models.Model):
    name = models.CharField(
        verbose_name='Publish house',
        max_length=50
    )

    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(
        verbose_name='Series of books',
        max_length=50
    )

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Genre of books',
        max_length=20
    )

    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(
        verbose_name='Name of books',
        max_length=50
    )
    Genre = models.ForeignKey(
        "directory.Genre",
        on_delete=models.PROTECT,
        verbose_name='Genre',
        related_name="Books"
    )
    description = models.TextField(
        verbose_name='Books discription',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy("directory:books-view", kwargs={"pk":self.pk})
    
