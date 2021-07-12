from django.contrib import admin
from django.contrib.auth.models import Group
from users.models import User

admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "is_active",
        "is_staff",
    )
    list_filter = ("is_active",)
    list_display_links = ("username",)


admin.site.register(User, UserAdmin)
