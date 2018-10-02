from django.contrib import admin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms

# Editting the supplied UserCreationForm found in the provided admin templates
# This form originally only entered new user information consisting of a username and password. 
class MyUserCreationForm(UserCreationForm):
    # Implementing a required email field
    email = forms.CharField(
        required=True, max_length=150, label='Email:', 
        help_text='Required. Please enter a valid email address.')
    # Implementing a required firstname field
    first_name = forms.CharField(
        required=True,max_length=250, label='First Name:',
        help_text='Please enter your first name.')
    # Implementing a required lastname field
    last_name = forms.CharField(
        required=True,max_length=250, label='Last Name:',
        help_text='Please enter your last name.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

# Remove the user group in preparartion for adding the above the new form to the above system
admin.site.unregister(User)

# UserAdmn is used to render the above form giving it the nice django admin look
class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm # Adding the new form
    add_fieldsets = ( # Adding new fields to the form
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')}
        ),
    )

# Adds the user group back into the system after changes to the UserCreation Form has been completed.
admin.site.register(User, MyUserAdmin)