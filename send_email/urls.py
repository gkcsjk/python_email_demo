from django.urls import path

from . import views

urlpatterns = [
  # /tutorial
  path('', views.home, name='home'),
  path('signin', views.sign_in, name='signin'),
  path('callback', views.callback, name='callback'),
  path('signout', views.sign_out, name='signout'),
  path('customers', views.customers, name='customers'),
  path('email', views.email, name='email'),
]