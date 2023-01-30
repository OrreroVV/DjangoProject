from datetime import datetime, date

from django.db import models

from video.models.employees.employees import Employees


class EmployeesAttendance(models.Model):
    job_number = models.ForeignKey(to=Employees, to_field='job_number', on_delete=models.CASCADE)
    day_date = models.CharField(max_length=20, default=datetime.strftime(date.today(), "%Y-%m-%d"))
    go_time = models.DateTimeField(auto_now_add=True)  # 首次创建时，自动设置上班时间
    off_time = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['job_number', 'day_date'], name='union_primary_key_password_id_number'),
        ]