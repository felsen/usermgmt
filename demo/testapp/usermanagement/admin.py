from django.contrib import admin
from usermanagement.models import Menus, RoleTypes, UserRoles, RoleConfiguration

admin.site.register(Menus)
admin.site.register(RoleTypes)
admin.site.register(UserRoles)
admin.site.register(RoleConfiguration)
