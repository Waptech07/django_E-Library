# Generated by Django 4.2 on 2023-09-06 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Library", "0025_remove_book_book_image_book_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="book_add_time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 9, 6, 10, 48, 39, 452039, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
