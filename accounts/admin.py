from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Create the AccountAdmin class by subclassing UserAdmin
class AccountAdmin(UserAdmin):
    # Specify which fields to display in the admin list view
    list_display = (
        'email',
        'first_name',
        'last_name',
        'username',
        'last_login',
        'date_joined',
        'is_active'
    )

    # Make the email, first name, and last name clickable in the list view
    list_display_links = ('email', 'first_name', 'last_name')

    # Specify which fields are read-only in the admin detail view
    readonly_fields = ('last_login', 'date_joined')

    # Specify the default ordering for the list view (by date_joined, in descending order)
    ordering = ('-date_joined',)

    # Fields to use with a ManyToMany relationship (not used here, so empty)
    filter_horizontal = ()

    # Fields to use for filtering (not used here, so empty)
    list_filter = ()

    # Specify the fieldsets for the admin detail view (not used here, so empty)
    fieldsets = ()


# Register the Account model with the custom AccountAdmin
admin.site.register(Account, AccountAdmin)
