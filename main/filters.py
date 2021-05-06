import django_filters

from .models import *


class ActorFilter(django_filters.FilterSet):
    class Meta:
        model = Actor
        fields = ['name', 'location', 'sex']


class RoleFilter(django_filters.FilterSet):
    class Meta:
        model = Role
        exclude = ['description', 'creator']
