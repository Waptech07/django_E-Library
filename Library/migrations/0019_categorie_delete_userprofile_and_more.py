# Generated by Django 4.2 on 2023-09-04 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Library", "0018_alter_book_book_add_date_alter_book_book_add_time_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categorie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_name", models.TextField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
        migrations.AlterField(
            model_name="book",
            name="book_add_time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 9, 4, 10, 28, 9, 345235, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
