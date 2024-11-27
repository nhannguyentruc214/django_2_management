from django.urls.conf import re_path, include
from tastypie.api import Api
from polls.api.resources import EntryResource,ProjectResource, EmployeeProjectResource, EmployeeResource, DepartmentResource
from django.urls import path

v1_api = Api(api_name='v1')
v1_api.register(EntryResource())
v1_api.register(ProjectResource())
v1_api.register(EmployeeProjectResource())
v1_api.register(EmployeeResource())
v1_api.register(DepartmentResource())

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("employee-success/", views.EmployeeSuccessView.as_view(), name="employee_success"),
    path("signup/", views.signup, name="signup"),
    path('list_employees/', views.EmployeeView.as_view(), name='list_employees'),
    re_path(r'^api/', include(v1_api.urls)),
]