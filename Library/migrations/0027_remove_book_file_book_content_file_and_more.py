# Generated by Django 4.2 on 2023-09-06 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Library", "0026_alter_book_book_add_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="file",
        ),
        migrations.AddField(
            model_name="book",
            name="content_file",
            field=models.FileField(
                default="book_content/link-expired.txt", upload_to="book_content/"
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="book_add_time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 9, 6, 11, 19, 30, 124416, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ImageField(
                default="book_images/default.png", upload_to="book_images/"
            ),
        ),
    ]
