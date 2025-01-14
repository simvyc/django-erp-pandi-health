from datetime import date
from django.db import models
from accounts.models import Doctor, Patient

class Record(models.Model):
    record_id = models.CharField(max_length=7, unique=True, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='records')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='records')
    visit_date = models.DateField(default=date.today)
    reason = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    lab_tests = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    prescription = models.TextField(blank=True, null=True)
    record_date = models.DateTimeField(auto_now_add=True)
    attachments = models.FileField(upload_to='medical_records/attachments/', blank=True, null=True)

    def __str__(self):
        return f"Record {self.record_id} - Diagnosis: {self.diagnosis} on {self.visit_date}"

    def save(self, *args, **kwargs):
        if not self.record_id:
            last_record = Record.objects.order_by('id').last()
            if last_record:
                # Extract numeric part from last record_id (e.g., "MD00001" -> 1)
                try:
                    last_id = int(last_record.record_id[2:])
                except ValueError:
                    last_id = 0  # In case of corrupted or invalid record_id
                new_id = f"MD{last_id + 1:05d}"  # Format as MD##### (e.g., MD00002)
            else:
                new_id = "MD00001"
            self.record_id = new_id
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Medical Record"
        verbose_name_plural = "Medical Records"
        ordering = ['-visit_date']
