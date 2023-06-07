# Generated by Django 4.2.1 on 2023-06-07 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0004_publish_alter_books_name_alter_genre_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='Genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Books', to='directory.genre', verbose_name='Genre'),
        ),
    ]
