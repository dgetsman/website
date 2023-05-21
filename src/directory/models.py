from django.db import models

class Genre(models.Model):
    name = models.CharField(
        verbose_name='Genre of books',
        max_length=30
    )

    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(
        verbose_name='Name of books',
        max_length=30
    )
    Genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        verbose_name='Genre'
    )
    description = models.TextField(
        verbose_name='Books discription',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
