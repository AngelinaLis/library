# Generated by Django 3.2.8 on 2021-10-25 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_birth_year', models.DateField(verbose_name='Год рождения автора')),
                ('book_written_year', models.DateField(verbose_name='Год издания книги')),
                ('book_title', models.CharField(db_index=True, max_length=124, verbose_name='Название книги')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]
