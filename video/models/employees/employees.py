from django.db import models


class Employees(models.Model):
    job_number = models.AutoField(primary_key=True)
    password = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=4)
    position = models.CharField(max_length=12)
    phone = models.CharField(max_length=16)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['password', 'id_number'], name='unique_password_id_number'),
        ]