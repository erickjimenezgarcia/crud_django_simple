from django.contrib import admin
from . import models


# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'country')


admin.site.register(models.Member, MemberAdmin)
