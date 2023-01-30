from django.contrib import admin
from video.models.administrator.administrator import Administrator
from video.models.equipment.equipment import Equipment
from video.models.employees.employees import Employees
from video.models.employees_attendance.employees_attendance import EmployeesAttendance
from video.models.violationInformation.violationInformation import ViolationInformation
from video.models.PatrolInspectionLog.patrolInspectionLog import PatrolInspectionLog
# Register your models here.
admin.site.register(Administrator)
admin.site.register(Equipment)
admin.site.register(Employees)
admin.site.register(EmployeesAttendance)
admin.site.register(ViolationInformation)
admin.site.register(PatrolInspectionLog)
