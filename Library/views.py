from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from datetime import date
from django.core.paginator import Paginator
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail


# ----------------- E-Library Management System Views -----------------

# Home Page
def index(request):
    books = Book.objects.all()[:4]
    categories = Categories.objects.all()

    return render(request, "index.html", {'books': books, 'categories': categories})


# Login Page
def login(request):

    # If request is post then get username and password from request
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate user
        user = auth.authenticate(username=username, password=password)

        # If user is authenticated then login user
        if user is not None:
            auth.login(request, user)

            # Redirect to home page
            return redirect("/")
        else:

            # If user is not authenticated then show error message
            # and redirect to login page
            messages.info(request, "Invalid Credential")
            return redirect("login")
    else:

        # If request is not post then render login page
        return render(request, "login.html")


# Register Page
def register(request):

    # If request is post then get user details from request
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # Check if password and confirm password matches
        if password == confirm_password:

            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect("register")

            # Check if email already exists
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already registered")
                return redirect("register")

            # If username and email does not exists then create user
            else:

                # Create user
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                )

                # Save user
                user.save()

                # Redirect to login page
                return redirect("login")
        else:

            # If password and confirm password does not matches then show error message
            messages.info(request, "Password does not match")
            return redirect("register")
    else:

        # If request is not post then render register page
        return render(request, "register.html")


# Logout view to logout user
def logout(request):

    # Logout user and redirect to home page
    auth.logout(request)
    return redirect("/login")


# Issue view to issue book to user
@login_required(login_url="login")
def issue(request):

    # If request is post then get book id from request
    if request.method == "POST":
        book_id = request.POST["book_id"]
        current_book = Book.objects.get(id=book_id)
        book = Book.objects.filter(id=book_id)
        issue_book = IssuedItem.objects.create(
            user_id=request.user, book_id=current_book
        )
        issue_book.save()
        book.update(quantity=book[0].quantity - 1)

        # Show success message and redirect to issue page
        messages.success(request, "Book issued successfully.")

    # Get all books which are not issued to user
    my_items = IssuedItem.objects.filter(
        user_id=request.user, return_date__isnull=True
    ).values_list("book_id")
    books = Book.objects.exclude(id__in=my_items).filter(quantity__gt=0)

    # Return issue page with books that are not issued to user
    return render(request, "issue_book.html", {"books": books})

# Return view to return book to library
@login_required(login_url="login")
def return_book(request):

    # If request is post then get book id from request
    if request.method == "POST":

        # Get book id from request
        book_id = request.POST["book_id"]

        # Get book object
        current_book = Book.objects.get(id=book_id)

        # Update book quantity
        book = Book.objects.filter(id=book_id)
        book.update(quantity=book[0].quantity + 1)

        # Update return date of book and show success message
        issue_book = IssuedItem.objects.filter(
            user_id=request.user, book_id=current_book, return_date__isnull=True
        )
        issue_book.update(return_date=date.today())
        messages.success(request, "Book returned successfully.")

    # Get all books which are issued to user
    my_items = IssuedItem.objects.filter(
        user_id=request.user, return_date__isnull=True
    ).values_list("book_id")

    # Get all books which are not issued to user
    books = Book.objects.exclude(~Q(id__in=my_items))

    # Return return page with books that are issued to user
    
    return render(request, "return_book.html", {"books": books})


# History view to show history of issued books to user
@login_required(login_url="login")
def history(request):

    # Get all issued books to user
    my_items = IssuedItem.objects.filter(user_id=request.user).order_by("-issue_date")

    # Paginate data
    paginator = Paginator(my_items, 10)

    # Get page number from request
    page_number = request.GET.get("page")
    show_data_final = paginator.get_page(page_number)

    # Return history page with issued books to user
    return render(request, "history.html", {"books": show_data_final})

def guest_user(request):
    
    # Get all books which are not issued to user
    books = Book.objects.all()[:4]
    categories = Categories.objects.all().values()

    return render(request, 'guest_user.html', {'books': books,'categories': categories,})

# contact form
def contact_us(request):
    if request.method == 'POST':
        name = request.POST["name"]
        from_email = request.POST["from_email"]
        message = request.POST["message"]
        
        try:
            send_mail(
                'Contact Form Submission',
                f'''Name: {name}
                    Email: {from_email}
                    Message: {message}''',
                from_email, #your email
                ['abdulfataiyakub02@gmail.com'], #Recipient email
                fail_silently=False,
            ),
            messages.success(request, 'Your message was sent successfully. We will get back to you soon.')
        except Exception as e:
            messages.error(request, f'Something went wrong. Please try again later. Error: {str(e)}')
        return redirect('contact_us')
    else:
        return render(request, 'contact_us.html')


@login_required(login_url="login")
def view_profile(request):
    datas = User.objects.all().values()
    # Get all issued books to user
    my_items = IssuedItem.objects.filter(user_id=request.user).order_by("-issue_date")[:5]
    
    context = {
        'datas' : datas,
        'books' : my_items
    }

    return render(request, 'profile/view_profile.html', context)

@login_required(login_url="login")
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        messages.success(request, 'Your profile has been updated successfully.')
        return redirect('edit_profile')

    else:

        return render(request, 'profile/edit_profile.html')
    
@login_required(login_url="login")
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST["confirm_new_password"]

         # Verify old password
        if not request.user.check_password(old_password):
            messages.error(request, 'Old password is incorrect.')
        elif new_password != confirm_new_password:
            messages.error(request, 'New passwords do not match.')
        else:
            # Change the password
            request.user.set_password(new_password)
            request.user.save()

            # Update the user's session to prevent them from being logged out
            update_session_auth_hash(request, request.user)

            messages.success(request, 'Your password has been changed successfully.')
            return redirect('change_password')

    
    return render(request, "profile/change_password.html")

@login_required(login_url="login")
def read_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    # Construct the full path to the book content file
    content_file_path = book.content_file.path

    # Serve the file as a response
    response = FileResponse(open(content_file_path, 'rb'))
    return response


