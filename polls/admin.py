from django.contrib import admin
from .models import Project, Employee, Department

class EmployeeInline(admin.StackedInline):
    model = Employee
    extra = 1
    show_change_link = True

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1
    show_change_link = True

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    def project_count(self, obj):
        return obj.projects.count()
    
    list_display = ('name', 'project_count')
    inlines = [ProjectInline]
    readonly_fields = ('project_count',)
    project_count.short_description = 'Number of Project'


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    def employee_count(self, obj):
        return obj.employees.count()
    
    list_display = ('title', 'employee_count')
    inlines = [EmployeeInline]
    employee_count.short_description = 'Number of Employee'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'participate_date', 'employee_role')
    search_fields = ('name', 'participate_date', 'employee_role')
