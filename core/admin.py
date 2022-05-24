from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import *


# Register your models here.
admin.site.register(Book)
admin.site.register(Journal)
admin.site.register(UserProfile)