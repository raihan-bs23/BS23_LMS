from django.contrib import admin
from . import models


class UserInfoAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'get_full_name',
        'contact_no',
        'profession',
        'user_role',
        'image_tag',
        'social_link',
    ]


# Register your models here.
admin.site.register(models.UserAdditionalInfo, UserInfoAdmin)
