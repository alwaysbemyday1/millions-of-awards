from django.contrib import admin

from .models import User, MajorCategory, MinorCategory, AwardsInfo


class UserAdmin(admin.ModelAdmin):
    fields = ['email', 'username']

class MajorCategoryAdmin(admin.ModelAdmin):
    fields = ['__all__']

class MinorCategoryAdmin(admin.ModelAdmin):
    fields = ['__all__']

class AwardsInfoAdmin(admin.ModelAdmin):
    fields = ['__all__']

admin.site.register(User, UserAdmin)
admin.site.register(MajorCategory, MajorCategoryAdmin)
admin.site.register(MinorCategory, MinorCategoryAdmin)
admin.site.register(AwardsInfo, AwardsInfoAdmin)
