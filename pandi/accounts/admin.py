from django.contrib import admin
from .models import Patient, Doctor

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'gender','is_active', 'family_doctor')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('gender', 'is_active', 'family_doctor')

    fields = (
        'user', 'first_name', 'last_name', 'gender', 
        'phone_number', 'email', 'address', 'city', 'state', 'zip_code', 'is_active', 'family_doctor'
    )
    # Read-only fields (e.g., registration date should not be editable)
    # readonly_fields = ('registration_date',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialty', 'email', 'phone_number', 'license_number', 'room_name', 'get_patients')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'license_number', 'specialty')
    list_filter = ('specialty', 'room_name')
    
    fieldsets = (
        ("Personal Information", {
            'fields': ('user', 'first_name', 'last_name', 'phone_number', 'email')
        }),
        ("Address Information", {
            'fields': ('residence_address', 'registration_address')
        }),
        ("Professional Details", {
            'fields': ('room_name', 'specialty', 'license_number')
        }),
        ("Emergency Contact", {
            'fields': ('contact_person_name', 'contact_person_phone')
        }),
        ("Additional Information", {
            'fields': ('allergies',)
        }),
    )
    
    ordering = ('last_name', 'first_name')
    
    readonly_fields = ('user', 'get_patients')
    
    def get_patients(self, obj):
        patients = obj.patients.all()  # Reverse relation from Doctor to Patient
        if patients.exists():
            return ", ".join([f"{patient.first_name} {patient.last_name}" for patient in patients])
        return "No patients assigned."
    get_patients.short_description = "Assigned Patients"

