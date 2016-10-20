from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Base(models.Model):
    """
    Common database fields are under base tables(Inheritance).
    """
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Menus(Base):
    """
    Menu and sub menu has added by the user
    """
    name = models.CharField("Menu Name", max_length=30)
    slug = models.SlugField("SEO friendly URL, use alphabets and hyphen",
        blank=True, null=True)
    parent = models.ForeignKey("self", blank=True, null=True)
    link = models.CharField("Link", max_length=20, blank=True, null=True)
    active = models.IntegerField(default=2)
    order = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True, 
    	related_name="%(class)s_relatedto_users")

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Menus"

    def __unicode__(self):
        return "%s" % (self.name)

    def get_submenu(self):
        return Menus.objects.filter(parent=self, active=2)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Menus, self).save(*args, **kwargs)


class RoleTypes(Base):
    """
    User Type has stored in this table Ex: Employee, Customer, etc,...
    """
    name = models.CharField("Role Name", max_length=50)
    slug = models.SlugField("SEO friendly URL, use alphabets and hyphen",
        blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True,
        related_name="%(class)s_related_users")
    active = models.IntegerField(default=2)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "RoleTypes"

    def __unicode__(self):
        return "%s" % (self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(RoleTypes, self).save(*args, **kwargs)


class UserRoles(Base):
    """
    User and the role type has stored in this table.
    """
    user = models.ForeignKey(User)
    role_type = models.ForeignKey(RoleTypes, related_name="%(class)s_related_roletypes")
    active = models.IntegerField(default=2)
    created_by = models.ForeignKey(User, blank=True, null=True,
        related_name="%(class)s_related_created_users")
    modified_by = models.ForeignKey(User, blank=True, null=True,
        related_name="%(class)s_related_modified_users")

    class Meta:
        ordering = ["user"]
        verbose_name_plural = "UserRoles"

    def __unicode__(self):
        return "%s" % (self.user.username)


class RoleConfiguration(Base):
    """
    Assigning the menu based permission in this table.
    """
    role = models.ForeignKey(RoleTypes, related_name="%(class)s_related_role_types")
    menu = models.ForeignKey(Menus, related_name="%(class)s_related_menus")
    add = models.IntegerField(blank=True, null=True)
    edit = models.IntegerField(blank=True, null=True)
    view = models.IntegerField(blank=True, null=True)
    delete = models.IntegerField(blank=True, null=True)
    search = models.IntegerField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(default=2)
    created_by = models.ForeignKey(User, blank=True, null=True,
        related_name="%(class)s_related_created_user")
    modified_by = models.ForeignKey(User, blank=True, null=True,
        related_name="%(class)s_related_modified_user")

    class Meta:
        ordering = ["role"]
        verbose_name_plural = "RoleConfiguration"

    def __unicode__(self):
        return "%s - %s" % (self.role.name, self.menu.name)
