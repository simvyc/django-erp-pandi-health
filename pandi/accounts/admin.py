from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Patient, Doctor

# Extend the default UserAdmin to use the custom User model
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'city')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name'),
        }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, UserAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'allergies')
    search_fields = ('user__username', 'user__email', 'allergies')

admin.site.register(Patient, PatientAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty', 'license_number')
    search_fields = ('user__username', 'user__email', 'specialty', 'license_number')

admin.site.register(Doctor, DoctorAdmin)

