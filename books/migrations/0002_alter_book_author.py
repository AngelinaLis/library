# Generated by Django 3.2.8 on 2021-10-26 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=124, verbose_name='Автор'),
        ),
    ]
