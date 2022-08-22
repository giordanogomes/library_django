# Generated by Django 4.1 on 2022-08-19 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
        ("book", "0011_borrowing_name_borrowed_anonymous_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowing",
            name="name_borrowed",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="user.user",
            ),
        ),
    ]