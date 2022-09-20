from django.contrib import admin
from rbac.models import *


# Register your models here.
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name"]
