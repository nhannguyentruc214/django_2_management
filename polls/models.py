from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    manager = models.OneToOneField(
        'Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='department_manager',
    )

    def __str__(self):
        return f"Department {self.name}"

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.IntegerField()
    def __str__(self):
        return f"Project {self.name}"

class Employee(models.Model):
    name = models.CharField(max_length=255)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    position = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    def __str__(self):
        return f"Employee {self.name}"

class EmployeeProject(models.Model):
    CHOICES = {
        "QC": "QualityAssurace",
        "FD": "FrontEndDev",
        "BD": "BackEndDev",
        "TT": "Tester"
    }

    def employee_name(self):
        return self.employee.name
    
    def project_name(self):
        return self.project.name
    
    role = models.CharField(max_length=255, choices=CHOICES)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_details')
    hours_worked = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projects_details')

    def __str__(self):
        return f"#{self.pk}"

