from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account,Profile,App,Task


# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name','last_name','last_login','username','date_joined','is_active')

    readonly_fields = ('last_login','date_joined')

    filter_horizontal =()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Account,AccountAdmin)
admin.site.register(App)
admin.site.register(Profile)
admin.site.register(Task)

