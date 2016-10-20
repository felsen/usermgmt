from django import template
from usermanagement.models import Menus, RoleTypes, UserRoles, RoleConfiguration
register = template.Library()


@register.filter
def get_user_menus(user):
    try:
        user_roles = UserRoles.objects.get(user__id=user.id)
        role_config_ids = RoleConfiguration.objects.filter(role=user_roles.role_type).only('menu').values_list('menu__id', flat=True)
        menus_items = Menus.objects.filter(id__in=map(int, role_config_ids), parent=None).order_by('order')
    except Exception as e:
        print "Error - get_user_menus [%s]"%(e.message)
        menus_items = []
    return menus_items


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
