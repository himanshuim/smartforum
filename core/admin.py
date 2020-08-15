from django.contrib import admin

from .models import Blog,Rank,Login,Question,Profile_info

admin.site.register(Blog)
admin.site.register(Rank)
admin.site.register(Login)
admin.site.register(Question)
admin.site.register(Profile_info)
