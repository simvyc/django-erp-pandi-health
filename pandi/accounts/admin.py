from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import CustomUser, Patient, Doctor


@admin.register(CustomUser)
class CustomUserAdmin(DefaultUserAdmin):
    model = CustomUser
    fieldsets = DefaultUserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'date_of_birth')}),
    )
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_doctor', 'is_patient')
    search_fields = ('email', 'username', 'first_name', 'last_name')

    def is_doctor(self, obj):
        return hasattr(obj, 'profile_doctor')  # Check if the user has a related Doctor profile
    is_doctor.boolean = True
    is_doctor.short_description = 'Doctor'

    def is_patient(self, obj):
        return hasattr(obj, 'profile_patient')  # Check if the user has a related Patient profile
    is_patient.boolean = True
    is_patient.short_description = 'Patient'


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'get_email', 'get_phone_number', 'get_gender', 'is_active', 'family_doctor')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'user__phone_number')
    list_filter = ('user__gender', 'is_active', 'family_doctor')

    # Display only fields that exist in the Patient model
    fields = ('user', 'is_active', 'family_doctor')

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_full_name.short_description = 'Full Name'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

    def get_phone_number(self, obj):
        return obj.user.phone_number
    get_phone_number.short_description = 'Phone Number'

    def get_gender(self, obj):
        return obj.user.gender
    get_gender.short_description = 'Gender'


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'specialty', 'get_email', 'get_phone_number', 'license_number', 'room_name', 'get_patients')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'user__phone_number', 'license_number', 'specialty')
    list_filter = ('specialty', 'room_name')

    fieldsets = (
        ("Personal Information", {
            'fields': ('user',)
        }),
        ("Professional Details", {
            'fields': ('room_name', 'specialty', 'license_number')
        }),
        ("Emergency Contact", {
            'fields': ('contact_person_name', 'contact_person_phone')
        }),
    )

    ordering = ('user__last_name', 'user__first_name')
    readonly_fields = ('get_patients',)

    def get_full_name(self, obj):
        return f"Dr. {obj.user.first_name} {obj.user.last_name}"
    get_full_name.short_description = 'Full Name'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

    def get_phone_number(self, obj):
        return obj.user.phone_number
    get_phone_number.short_description = 'Phone Number'

    def get_patients(self, obj):
        patients = obj.patients.all()
        if patients.exists():
            return ", ".join([f"{patient.user.first_name} {patient.user.last_name}" for patient in patients])
        return "No patients assigned."
    get_patients.short_description = "Assigned Patients"
