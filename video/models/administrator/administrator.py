from django.db import models


class Administrator(models.Model):
    admin_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=8)
    id_number = models.CharField(max_length=20)
    phone = models.CharField(max_length=16)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['password'], name='unique_password'),
        ]