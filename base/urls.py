from django.urls import path
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import auth
from .views import register_admin, register_manager, register_agent, register_guest
from base import views
from .views import reset_password
from django.urls import path
from .views import custom_login
from .views import CustomPasswordResetCompleteView



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
]
 