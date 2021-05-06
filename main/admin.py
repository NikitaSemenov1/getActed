from django.contrib import admin

from main.models import *

admin.site.register(Actor)
admin.site.register(Employer)
admin.site.register(Role)
admin.site.register(RequestRoleToActor)
admin.site.register(RequestActorToRole)
