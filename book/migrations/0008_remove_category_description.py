# Generated by Django 4.1 on 2022-08-17 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_book_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
