from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('record_id', 'patient', 'doctor', 'visit_date', 'diagnosis', 'record_date')
    search_fields = ('record_id', 'patient__first_name', 'patient__last_name', 'doctor__first_name', 'doctor__last_name', 'diagnosis')
    list_filter = ('visit_date', 'doctor', 'patient')
    readonly_fields = ('record_date',)
    ordering = ['-visit_date']

    fieldsets = (
        ("Basic Information", {
            'fields': ('patient', 'doctor', 'visit_date')
        }),
        ("Medical Details", {
            'fields': ('reason', 'diagnosis', 'lab_tests', 'treatment', 'prescription')
        }),
        ("Attachments and Meta", {
            'fields': ('attachments', 'record_date')
        }),
    )
