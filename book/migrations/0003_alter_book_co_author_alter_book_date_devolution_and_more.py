# Generated by Django 4.1 on 2022-08-15 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_rename_registerbook_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='co_author',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_devolution',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_rented',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name_rented',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='time_duration',
            field=models.DateField(blank=True),
        ),
    ]
