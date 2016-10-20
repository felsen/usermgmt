"""testapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from usermanagement import views

urlpatterns = [
    url(r'-manage/', views.menus),

    url(r'-add-menu/', views.add_menus),
    url(r'-edit-menu/(?P<menuid>\d+)/', views.edit_menus),

    url(r'-add-role-type/', views.add_role_type),
    url(r'-edit-role-type/(?P<roleid>\d+)/', views.edit_role_type),

    url(r'-add-user-role/', views.add_user_role),
    url(r'-edit-user-role/(?P<uroleid>\d+)/', views.edit_user_role),

    url(r'-add-role-config/(?P<roleid>\d+)/', views.add_role_config),
]
