from django.contrib import admin
from accounts.models import User, Customer, Agent
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("id", "username", "email", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "role")
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {"fields": (
            "is_active",
            "is_staff",
            "is_superuser",
        ), }),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', "role"),
        }),
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'city', 'created_at']


@admin.register(Agent)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name' , 'phone', 'city', 'created_at']
