from django.db import models

class Department(models.Model):
    title = models.CharField(max_length=255)
    manager = models.OneToOneField(
        'Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='department_manager',
    )

    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    participate_date = models.DateField()
    end_date = models.DateField()
    budget = models.IntegerField()
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    position = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class EmployeeProject(models.Model):
    HoursWorked = models.IntegerField()
    CHOICES = {
        "QC": "QualityAssurace",
        "FD": "FrontEndDev",
        "BD": "BackEndDev",
        "TT": "Tester"
    }
    employee_role = models.CharField(max_length=255, choices=CHOICES)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employeeDetails')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projectsDetails')

    def __str__(self):
        return f"EmployeeProject {self.pk}"

