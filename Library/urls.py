# Importing required libraries
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


# Url patterns for Books app module of Library Management System
urlpatterns = [
    path("", views.index, name="index"),
    path("issue/", views.issue, name="issue"),
    path("return_book/", views.return_book, name="return_book"),
    path("history/", views.history, name="history"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('guest_user/', views.guest_user, name='guest_user'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change_password/', views.change_password, name='change_password'),
    path('contact/', views.contact_us, name='contact_us'),
    path('read_book/<int:book_id>/', views.read_book, name='read_book'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
