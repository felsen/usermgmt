from django.forms import ModelForm
from django.contrib.auth.models import User
from usermanagement.models import Menus, RoleTypes, UserRoles, RoleConfiguration


class MenuForm(ModelForm):
    """
    Adding the menus list using the menu form.
    """
    class Meta:
        model = Menus
        exclude = ('slug', 'active', 'created_by')


class RoleTypesForm(ModelForm):
    """
    Adding all the role types using the role type form.
    """
    class Meta:
        model = RoleTypes
        exclude = ('slug', 'active', 'created_by')


class UserRolesForm(ModelForm):
    """
    Adding the roles for the every user by user roles form.
    """
    class Meta:
        model = UserRoles
        exclude = ('slug', 'active', 'created_by', 'modified_by')
