from django.urls.conf import path, re_path, include
from tastypie.api import Api
from polls.api.resources import EntryResource,ProjectResource, EmployeeProjectResource, EmployeeResource, DepartmentResource

v1_api = Api(api_name='v1')
v1_api.register(EntryResource())
v1_api.register(ProjectResource())
v1_api.register(EmployeeProjectResource())
v1_api.register(EmployeeResource())
v1_api.register(DepartmentResource())

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^api/', include(v1_api.urls)),
]