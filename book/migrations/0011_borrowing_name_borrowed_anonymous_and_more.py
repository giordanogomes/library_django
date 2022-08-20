# Generated by Django 4.1 on 2022-08-19 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
        ("book", "0010_rename_rented_book_borrowed_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="borrowing",
            name="name_borrowed_anonymous",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="borrowing",
            name="name_borrowed",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="user.user",
            ),
            preserve_default=False,
        ),
    ]
