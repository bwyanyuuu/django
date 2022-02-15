from django.contrib import admin
from main.models import MyUser

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(MyUser, AuthorAdmin)
# Register your models here.
