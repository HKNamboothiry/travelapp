from django.contrib import admin

# Register your models here.

from . models import Place, TeamMembers

admin.site.register(Place)
admin.site.register(TeamMembers)