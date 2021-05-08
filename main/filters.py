import django_filters

from .models import *


class ActorFilter(django_filters.FilterSet):
    class Meta:
        model = Actor
        fields = ['name', 'location', 'sex', 'height', 'weight', 'eye_color', 'hair_color', 'race', 'nation',
                  'body_type']


class RoleFilter(django_filters.FilterSet):
    class Meta:
        model = Role
        exclude = ['description', 'creator']
