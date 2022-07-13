from django.contrib import admin
from .models import Select, Address

class SelectAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'price')

    fieldset = (
        (None, {
            'fields': ('item', 'quantity', 'price')
        }),
    ),

class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'state', 'country', 'postalcode')

    fieldset = (
        (None, {
            'fields': ('address', 'state', 'country', 'postalcode')
        }),
    ),
    
admin.site.register(Select, SelectAdmin)
admin.site.register(Address, AddressAdmin)
