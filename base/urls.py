from django.urls import path
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import auth
from base import views
from .views import reset_password
from django.urls import path
from .views import custom_login
from .views import CustomPasswordResetCompleteView
from .views import get_book_reviews
from .views import bookscategory,book_list, book_list2, book_list3, book_list4
from .views import logout_view,about_us
from . import views


urlpatterns=[
  path('home/', views.home, name='home'),
  path('signup/custom_login/home/', views.home , name='Library'),
  path('', views.login_view , name='login'),
  path('custom_login/', custom_login, name='custom_login'),
  path('custom_login/home/', views.home , name='Library'),
  path('signup/', views.signup, name='signup'),
  path('forgot-password/', views.forgot_password, name='forgot-password'),
  path('reset-password/',reset_password, name='reset-password'),
  path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
  path('home/blog_view/', views.blog, name='reader_view'),
  path('feedback/', views.feedback_view, name='feedback'),
  path('feedback_thanks/', views.feedback_thanks, name='feedback_thanks'),
  path('get_book_reviews/', get_book_reviews, name='get_book_reviews'),
  path('books-category/', bookscategory, name='bookscategory'),
  path('logout/', logout_view, name='logout'),
  path('book_list/', book_list, name='book_list'),
  path('book_list2/', book_list2, name='book_list2'),
  path('book_list3/', book_list3, name='book_list3'),
  path('book_list4/', book_list4, name='book_list4'),
  path('about_us/', about_us, name='about_us'),
  path('select_books/', views.select_books, name='select_books'),
  path('selected_books/', views.selected_books, name='selected_books'),
]
 