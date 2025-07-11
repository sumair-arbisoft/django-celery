from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

    def is_pitched(self, obj):
        return obj.profile.is_pitched if hasattr(obj, 'profile') else ''
    is_pitched.short_description = 'Pitched'

    def is_pitched_at(self, obj):
        return obj.profile.is_pitched_at if hasattr(obj, 'profile') else ''
    is_pitched_at.short_description = 'Pitched At'

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_pitched', 'is_pitched_at')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
