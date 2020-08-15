from django.contrib import admin
from django.urls import path,include
from .views import home_page
# from .views import login 
from .views import register
from .views import profile
from .views import blog
from .views import rank
from .views import login,log_out


urlpatterns = [
    path('', home_page),
    path('profile/',profile),
    path('blog/',blog),
    path('rank/',rank),
    # path('profile',profile_info),
    
]