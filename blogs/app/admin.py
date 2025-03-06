from django.contrib import admin
from .models import Login,Information
# Register your models here.

class loginAdmin(admin.ModelAdmin):
    list_display = ['username','password']

class InforAdmin(admin.ModelAdmin):
    list_display = ["infor"]


admin.site.register(Login,loginAdmin)
admin.site.register(Information,InforAdmin)