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
from django.contrib import admin
from usermanagement import views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),

    url(r'^register/$', CreateView.as_view(template_name='register.html', form_class=UserCreationForm, success_url='/login/')),

    url(r'^home/$', views.home, name="home"),

    url(r'^user', include('usermanagement.urls')),

#    url(r'^manage/', views.menus),

#    url(r'^add-menu/', views.add_menus),
#    url(r'^edit-menu/(?P<menuid>\d+)/', views.edit_menus),

#    url(r'^add-role-type/', views.add_role_type),
#    url(r'^edit-role-type/(?P<roleid>\d+)/', views.edit_role_type),

#    url(r'^add-user-role/', views.add_user_role),
#    url(r'^edit-user-role/(?P<uroleid>\d+)/', views.edit_user_role),

#    url(r'^add-role-config/(?P<roleid>\d+)/', views.add_role_config),
]
