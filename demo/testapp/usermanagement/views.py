from django.shortcuts import render
from usermanagement.models import Menus, RoleTypes, UserRoles, RoleConfiguration
from usermanagement.forms import MenuForm, RoleTypesForm, UserRolesForm


def home(request):
    return render(request, 'index.html', locals())

def menus(request):
    return render(request, 'home.html', locals())

def add_menus(request):
    key = "Add"
    obj = Menus.objects.all()
    form = MenuForm()
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            obj = Menus.objects.filter(name=request.POST.get("name"))
            if obj:
                form.errors['name'] = form.error_class(['Menu with this name already exists'])
            else:
                form.save()
    return render(request, 'menus.html', locals())

def edit_menus(request, menuid):
    key = "Edit"
    obj = Menus.objects.all()
    menu_obj = Menus.objects.get(id=int(menuid))
    form = MenuForm(instance=menu_obj)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu_obj)
        if form.is_valid():
            menuobj = Menus.objects.filter(name__iexact=request.POST.get("name")).exclude(id=menuid)
            if menuobj:
                form.errors['name'] = form.error_class(['Menu with this name already exists'])
            else:
                form.save()
    return render(request, 'menus.html', locals())


def add_role_type(request):
    obj = RoleTypes.objects.all()
    key = "Add"
    form = RoleTypesForm()
    if request.method == "POST":
        form = RoleTypesForm(request.POST)
        if form.is_valid():
            obj = RoleTypes.objects.filter(name=request.POST.get("name"))
            if obj:
                form.errors['name'] = form.error_class(['Role with this name already exists'])
            else:
                form.save()
    return render(request, 'roletype.html', locals())


def edit_role_type(request, roleid):
    obj = RoleTypes.objects.all()
    key = "Edit"
    role_obj = RoleTypes.objects.get(id=int(roleid))
    form = RoleTypesForm(instance=role_obj)
    if request.method == 'POST':
        form = RoleTypesForm(request.POST, instance=role_obj)
        if form.is_valid():
            roleobj = RoleTypes.objects.filter(name__iexact=request.POST.get("name")).exclude(id=roleid)
            if roleobj:
                form.errors['name'] = form.error_class(['Role with this name already exists'])
            else:
                form.save()
    return render(request, 'roletype.html', locals())


def add_user_role(request):
    obj = UserRoles.objects.all()
    key = "Add"
    form = UserRolesForm()
    if request.method == 'POST':
        form = UserRolesForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'userrole.html', locals())


def edit_user_role(request, uroleid):
    key = "Edit"
    obj = UserRoles.objects.all()
    rolobj = UserRoles.objects.get(id=int(uroleid))
    form = UserRolesForm(instance=rolobj)
    if request.method == 'POST':
        form = UserRolesForm(request.POST, instance=rolobj)
        if form.is_valid():
            form.save()
    return render(request, 'userrole.html', locals())


def add_role_config(request, roleid):
    menu = Menus.objects.all()
    if request.method == "POST":
        menu = request.POST.getlist('menu')
        role_obj = RoleTypes.objects.get(id=roleid)
        if role_obj and menu:
            for i in menu:
                menu_obj =  Menus.objects.get(pk=int(i))
                add = request.POST.get('add_'+str(i)+'_'+str(role_obj.pk))
                edit = request.POST.get('edit_'+str(i)+'_'+str(role_obj.pk))
                delete = request.POST.get('delete_'+str(i)+'_'+str(role_obj.pk))
                view = request.POST.get('view_'+str(i)+'_'+str(role_obj.pk))
                report = request.POST.get('report_'+str(i)+'_'+str(role_obj.pk))
                search = request.POST.get('search_'+str(i)+'_'+str(role_obj.pk))
                role_config, created = RoleConfiguration.objects.get_or_create(role=role_obj, menu=menu_obj)
                role_config.add = 2 if add == 'True' else None
                role_config.edit = 2 if edit == 'True' else None
                role_config.view = 2 if view == 'True' else None
                role_config.delete = 2 if delete == 'True' else None
                role_config.report = 2 if report == 'True' else None
                role_config.search = 2 if search == 'True' else None
                role_config.save()         
    return render(request, 'roleconfig.html', locals())
