# Generated by Django 4.2 on 2023-09-06 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Library", "0031_alter_book_book_add_time_alter_book_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="book_add_time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 9, 6, 13, 20, 34, 955407, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
