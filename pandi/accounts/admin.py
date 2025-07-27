from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, Doctor, Patient


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = (
        'email', 'first_name', 'last_name', 'is_doctor', 'is_patient', 'is_staff', 'is_superuser', 'registration_date', 
    )
    list_filter = ('is_staff', 'is_superuser', 'gender', 'city')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-registration_date',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
            'fields': (
                'first_name', 'last_name', 'phone_number',
                'date_of_birth', 'gender', 'address', 'city', 'state', 'zip_code'
            )
        }),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'registration_date')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ('groups', 'user_permissions',)
    readonly_fields = ('registration_date',)

    def is_doctor(self, obj):
        return hasattr(obj, 'doctor')
    is_doctor.boolean = True
    is_doctor.short_description = 'Doctor'

    def is_patient(self, obj):
        return hasattr(obj, 'patient')
    is_patient.boolean = True
    is_patient.short_description = 'Patient'


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'user_email', 'first_name', 'last_name', 'speciality',
        'room_name', 'license_number', 'is_active'
    )
    search_fields = ('user__email', 'speciality', 'license_number', 'user__first_name', 'user__last_name')
    list_filter = ('speciality', 'is_active')
    readonly_fields = ('is_active',)

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = "Email"

    def first_name(self, obj):
        return obj.user.first_name
    first_name.short_description = "First Name"

    def last_name(self, obj):
        return obj.user.last_name
    last_name.short_description = "Last Name"


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'first_name', 'last_name', 'family_doctor', 'is_active')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    list_filter = ('is_active', 'family_doctor')
    readonly_fields = ('is_active',)

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = "Email"

    def first_name(self, obj):
        return obj.user.first_name
    first_name.short_description = "First Name"

    def last_name(self, obj):
        return obj.user.last_name
    last_name.short_description = "Last Name"
