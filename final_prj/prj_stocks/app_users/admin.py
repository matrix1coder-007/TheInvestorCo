from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group
from .models import CustomUserModel

admin.site.unregister(Group)

class CustomUserAdmin(admin.ModelAdmin):

    list_display = ['full_name', 'user_email']

    fieldsets = (
        ('Personal Details', {
            'fields': (
                'user_email',
                'user_fname',
                'user_mname',
                'user_lname',
                'password'
            ),
        }),
        ('Official Details',
         {
             'fields': (
                 'user_registered',
                 'is_superuser',
                 'is_customer',
                 'is_staff',
                 'user_deactivation_dt'
             ), }),

    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)


admin.site.register(CustomUserModel, CustomUserAdmin)
