from django.contrib import admin

# Register your models here.
from sbin.models import Bin,User

admin.site.register(Bin)
admin.site.register(User)