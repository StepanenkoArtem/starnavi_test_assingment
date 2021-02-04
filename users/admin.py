from django.contrib import admin
from django.contrib.auth import forms
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin
from users.models import SocialUser


class SocialUserForm(forms.UserChangeForm):
    username = None

    class Meta:
        model = SocialUser
        fields = ()


class SocialUserAddForm(forms.UserCreationForm):
    username = None

    class Meta:
        model = SocialUser
        fields = ()


class UserAdmin(UserBaseAdmin):
    form = SocialUserForm
    add_form = SocialUserAddForm

    list_display = (
        'email',
        'is_active',
        'is_staff',
        'is_superuser',
        'facebook',
        'avatar',
        'date_joined',
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'is_active', '-date_joined')
    exclude = ('username',)

    fieldsets = (
        (
            None,
            {
                'classes': ('extrapretty',),
                'fields': ('email', 'first_name', 'last_name', 'is_active'),
            },
        ),
        (
            'Advanced Options',
            {
                'classes': ('wide',),
                'fields': ('github', 'phone'),
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('extrapretty',),
                'fields': ('email', 'first_name', 'last_name', 'is_active'),
            },
        ),
        (
            'Paswword',
            {
                'classes': ('wide',),
                'fields': ('password1', 'password2'),
            },
        )
    )


admin.site.register(SocialUser, UserAdmin)
