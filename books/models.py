from django.db import models
from django.contrib.auth.models import User
from django import forms

class Book(models.Model):
    author = models.CharField(max_length=124, verbose_name='Автор')
    author_birth_year = models.PositiveIntegerField(verbose_name='Год рождения автора')
    book_written_year = models.PositiveIntegerField(verbose_name='Год издания книги')
    book_title = models.CharField(max_length=124, db_index=True, verbose_name='Название книги')

    def __str__(self):
        return self.book_title
