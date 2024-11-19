from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from  .forms import CustomUserChangeForm, CustomUserCreationForm



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'full_name', 'status']


    fieldsets = UserAdmin.fieldsets + (
        ('реквизиты 1С', {'fields': ('full_name', 'status',)}),
    )


    add_fieldsets = UserAdmin.add_fieldsets + (
        ('реквизиты 1С', {'fields': ('full_name', 'status',)}),
    )

    search_fields = ('full_name', 'username',)
    ordering = ('full_name', 'username',)
    list_filter = ('status',)

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
