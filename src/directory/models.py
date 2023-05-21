from django.db import models

class Genre(models.Model):
    name = models.CharField(
        verbose_name='Genre of books',
        max_length=30
    )
    description = models.TextField(
        verbose_name='Genre discription',
        null=True,
        blank=True
    )
