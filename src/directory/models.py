from django.db import models
from django.urls import reverse_lazy
from pathlib import Path
from PIL import Image

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
    picture = models.ImageField(
        verbose_name="Picture",
        upload_to="uploads/%Y/%m/%d/"
    )
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
    
    def book_picture_med(self):
        original_url = self.picture.url
        new_url = original_url.split('.')
        picture_url = ".".join(new_url[:-1]) + "_150_." + new_url[-1]
        return picture_url
    
    def book_picture_small(self):
        original_url = self.picture.url
        new_url = original_url.split('.')
        picture_url = ".".join(new_url[:-1]) + "_40_." + new_url[-1]
        return picture_url
    
    def picture_resizer(self):
        extention = self.picture.file.name.split('.')[-1]
        BASE_DIR = Path(self.picture.file.name).resolve().parent
        file_name = Path(self.picture.file.name).resolve().name.split('.')
        for m_basewidth in [150, 40]:
            m_basewidth = 150
            im = Image.open(self.picture.file.name)
            wpercent = (m_basewidth/float(im.size[0]))
            hsize = int((float(im.size[1])*float(wpercent)))
            im.thumbnail((m_basewidth,hsize), Image.Resampling.LANCZOS)
            im.save(BASE_DIR / "".join(file_name[:-2]) + f'_{m_basewidth}_.' + extention)