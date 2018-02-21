from django import template
from usermgmt.models import Menus, RoleTypes, RoleConfiguration
register = template.Library()


@register.filter
def get_menu_values(menu_pk, roleid):
    val_dict = {}
    try:
        menu = Menus.objects.get(pk=int(menu_pk))
        role = RoleTypes.objects.get(pk=roleid)
        role_config = RoleConfiguration.objects.get(menu=menu, role=role)
        val_dict['add'] = role_config.add
        val_dict['edit'] = role_config.edit
        val_dict['view'] = role_config.view
        val_dict['delete'] = role_config.delete
        val_dict['report'] = role_config.report
        val_dict['search'] = role_config.search
    except Exception:
        val_dict = {
            'add': None,
            'edit': None,
            'view': None,
            'delete': None,
            'report': None,
            'search': None
            }
    return val_dict
