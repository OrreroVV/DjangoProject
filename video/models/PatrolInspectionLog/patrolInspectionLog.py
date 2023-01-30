from datetime import datetime, date

from django.db import models
from video.models.equipment.equipment import Equipment


class PatrolInspectionLog(models.Model):
    equipment_id = models.ForeignKey(to=Equipment, to_field='equipment_id', on_delete=models.CASCADE)
    record_date = models.CharField(max_length=20, default=datetime.strftime(date.today(), "%Y-%m-%d"))
    violations_number = models.IntegerField()
    manage_name = models.CharField(max_length=10)
    video_url = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['record_date', 'equipment_id'], name='union_primary_key_record_date_equipment_id'),
        ]