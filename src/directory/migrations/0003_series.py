# Generated by Django 4.2.1 on 2023-05-22 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Series of books')),
            ],
        ),
    ]
