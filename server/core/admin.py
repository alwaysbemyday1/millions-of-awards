from django.contrib import admin

from .models import User, MajorCategory, MinorCategory, AwardsInfo, Ceremony, Nominee


class UserAdmin(admin.ModelAdmin):
    fields = ['email', 'username']

class MajorCategoryAdmin(admin.ModelAdmin):
    fields = []

class MinorCategoryAdmin(admin.ModelAdmin):
    fields = []

class AwardsInfoAdmin(admin.ModelAdmin):
    fields = []

class CeremonyAdmin(admin.ModelAdmin):
    fields = []

class NomineeAdmin(admin.ModelAdmin):
    fields = []

admin.site.register(User, UserAdmin)
admin.site.register(MajorCategory, MajorCategoryAdmin)
admin.site.register(MinorCategory, MinorCategoryAdmin)
admin.site.register(AwardsInfo, AwardsInfoAdmin)
admin.site.register(Ceremony, CeremonyAdmin)
admin.site.register(Nominee, NomineeAdmin)