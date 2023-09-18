# Generated by Django 4.2 on 2023-09-03 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Library", "0011_alter_book_book_add_time_alter_book_book_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="book_add_time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 9, 3, 8, 18, 50, 260057, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="book_image",
            field=models.ImageField(
                blank="True", upload_to="Library\templates\\images"
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="file",
            field=models.FileField(
                null=True, upload_to="Library/templates/files", verbose_name="file "
            ),
        ),
    ]
