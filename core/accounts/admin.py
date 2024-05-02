from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.user import CustomUser
from .models.profile import Profile

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff','is_active',)
    list_filter = ('is_staff', 'is_active')
    searching_fields = ("email",)
    ordering = ('email',)
    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("email", "password"),
            },
        ),
        (
            "permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
        (
            "group permissions",
            {
                "classes":("collapse",),
                "fields": ("groups", "user_permissions"),
            },
        ),
        (
            "important date",
            {
                "fields": ("last_login",),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
    )

admin.site.register(Profile)
admin.site.register(CustomUser, CustomUserAdmin)
