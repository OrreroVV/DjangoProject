from django.db import models

from video.models.employees.employees import Employees
from video.models.equipment.equipment import Equipment


class ViolationInformation(models.Model):
    violation_id = models.AutoField(primary_key=True)
    job_number = models.ForeignKey(to=Employees, to_field='job_number', on_delete=models.CASCADE)
    equipment_id = models.ForeignKey(to=Equipment, to_field='equipment_id', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    violation_type = models.CharField(max_length=12)

