from tastypie.resources import ModelResource
from polls.models import Entry


class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        allowed_methods = ['get']
        resource_name = 'entry'
