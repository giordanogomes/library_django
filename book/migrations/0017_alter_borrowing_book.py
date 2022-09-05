# Generated by Django 4.1 on 2022-09-01 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0016_remove_borrowing_name_borrowed_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowing",
            name="book",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="book.book",
                verbose_name="Livro",
            ),
        ),
    ]
