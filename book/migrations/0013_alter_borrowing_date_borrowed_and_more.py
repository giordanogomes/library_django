# Generated by Django 4.1 on 2022-08-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0012_alter_borrowing_name_borrowed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowing",
            name="date_borrowed",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="borrowing",
            name="date_devolution",
            field=models.DateField(blank=True, null=True),
        ),
    ]
