from tastypie.resources import ModelResource
from polls.models import Entry, Project, Employee, Department, EmployeeProject
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication

class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        allowed_methods = ['get','put']
        resource_name = 'entry'
        authentication = Authentication()
        authorization = Authorization() # THIS IS IMPORTANT

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        allowed_methods = ['get','delete']
        resource_name = 'project'
        authentication = Authentication()
        authorization = Authorization() # THIS IS IMPORTANT

class DepartmentResource(ModelResource):
    class Meta:
        queryset = Department.objects.all()
        allowed_methods = ['get', 'post']
        resource_name = 'department'
        authentication = Authentication()
        authorization = Authorization() # THIS IS IMPORTANT

class EmployeeResource(ModelResource):
    department = fields.ForeignKey(DepartmentResource, 'department')
    class Meta:
        queryset = Employee.objects.all()
        allowed_methods = ['get']
        resource_name = 'employee'

class EmployeeProjectResource(ModelResource):
    employee = fields.ForeignKey(EmployeeResource, 'employee')
    project = fields.ForeignKey(ProjectResource, 'project')
    class Meta:
        queryset = EmployeeProject.objects.all()
        allowed_methods = ['get']
        resource_name = 'employeeProject'
