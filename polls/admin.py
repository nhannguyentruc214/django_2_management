from django.contrib import admin
from .models import  Entry, Project, Employee, Department, EmployeeProject

class EmployeeInline(admin.StackedInline):
    model = Employee
    extra = 1
    show_change_link = True

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1
    show_change_link = True

class EmployeeProjectInline(admin.TabularInline):
    model = EmployeeProject
    extra = 1
    show_change_link = True

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
     
    def get_manager(self, obj):
        return obj.department.manager
    
    list_display = ('name', 'salary', 'date_of_birth','position','get_manager')
    inlines = [EmployeeProjectInline]
    get_manager.short_description = "Employee's manager"

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    def employee_count(self, obj):
        return obj.employees.count()
    
    def get_manager(self, obj):
        return obj.manager
    
    list_display = ('name', 'employee_count','get_manager')
    inlines = [EmployeeInline]
    employee_count.short_description = 'Number of Employee'
    get_manager.short_description = 'Department manager'

@admin.register(EmployeeProject)
class EmployeeProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_name','project_name','role','hours_worked',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date','end_date', 'budget')
    search_fields = ('name', 'start_date', 'end_date,' ,'budget')
    inlines=[EmployeeProjectInline]

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug','body')
