from django.contrib import admin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms


class MyUserCreationForm(UserCreationForm):
    email = forms.CharField(
        required=True, max_length=150, label='Email:', 
        help_text='Required. Please enter a valid email address.')
    first_name = forms.CharField(
        required=True,max_length=250, label='First Name:',
        help_text='Please enter your first name.')
    last_name = forms.CharField(
        required=True,max_length=250, label='Last Name:',
        help_text='Please enter your last name.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


admin.site.unregister(User)

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')}
        ),
    )

admin.site.register(User, MyUserAdmin)