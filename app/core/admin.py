"""
Django admin customization .
"""


from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin  import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import  gettext_lazy as translate


class UserAdmin(BaseUserAdmin):
    """Define the admin page for users ."""
    ordering=['id']
    list_display=['email','name']
    fieldsets=(
        (None,{'fields':('email','password','name')}),
        (
            translate('permissions'),
            {
                'fields':(
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (translate('Importantes dates'),{'fields':('last_login',)})
  
    )
    readonly_fields=['last_login']
    add_fieldsets=(
             (None,{
                 'classes':('wide',),
                 'fields':(
                     'email',
                     'password1',
                     'password2',
                     'name',
                     'is_active',
                     'is_staff',
                     'is_superuser',
                 ),
             }),
    )

admin.site.register(models.User,UserAdmin)
