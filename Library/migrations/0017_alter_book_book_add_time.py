# Generated by Django 4.2 on 2023-09-03 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Library", "0016_alter_book_book_add_time_alter_issueditem_issue_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="book_add_time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 9, 3, 19, 39, 16, 274043, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
