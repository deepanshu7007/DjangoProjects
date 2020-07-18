from django.contrib import admin
from Login.models import UserLogin

class LoginDetails(admin.ModelAdmin):
    list_display=['UserName','Passwords'];


admin.site.register(UserLogin,LoginDetails);

