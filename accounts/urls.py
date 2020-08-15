from django.contrib import admin
from django.urls import path, include

from .views import login_page,register_page

app_name= 'accounts'

urlpatterns = [
    path('login',login_page, name='login_page'),
    path('register',register_page,name='register_page')
    # path('profile',profile_info),
    
]