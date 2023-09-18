from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

# ----------- E-Library Management System Models ------------

# Book model to store book details
class Book(models.Model):
    image = models.ImageField(upload_to='book_images/', default='book_images/default_big.png')
    book_name = models.CharField(max_length=150)
    author_name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    content_file = models.FileField(upload_to='book_content/', default='book_content/link-expired.txt')
    subject = models.CharField(max_length=2000)
    book_add_time = models.TimeField(default=timezone.now())
    book_add_date = models.DateField(default=date.today())

    class Meta:
        unique_together = ("book_name", "author_name")

    def __str__(user):
        return user.book_name


# IssuedItem model to store issued book details
class IssuedItem(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField(default=date.today(), blank=False)
    return_date = models.DateField(blank=True, null=True)

    # property to get book name
    @property
    def book_name(user):
        return user.book_id.book_name

    # property to get author name
    @property
    def username(user):
        return user.user_id.author_name

    def __str__(user):
        return (
            user.book_id.book_name
            + " read by "
            + user.user_id.first_name
            + " on "
            + str(user.issue_date)
        )
    
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(user):
        return f"{user.first_name} - {user.last_name}"

class Categories(models.Model):
    category_name = models.CharField(max_length=100)

    # property to get book name
    @property
    def book_name(user):
        return user.category_name

    def __str__(user):
        return f"{user.category_name}"

