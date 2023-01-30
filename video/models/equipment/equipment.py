from django.db import models
from django.contrib.auth.models import User


class Equipment(models.Model):
    equipment_id = models.CharField(primary_key=True, max_length=18)
    type = models.CharField(max_length=10)
    purchase_time = models.DateTimeField()
    purchase_business = models.CharField(max_length=20)
    usage = models.CharField(max_length=10)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(type='无人机') | models.Q(type='监控'), name="check_type"),
            models.CheckConstraint(
                check=models.Q(usage='极好') | models.Q(usage='良好') | models.Q(usage='不佳') | models.Q(usage='报废'), name="check_usage"),
        ]
