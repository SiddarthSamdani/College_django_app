from django.contrib import admin
from .models import Notice
from django.contrib.admin.options import ModelAdmin
from .models import Branch, Profile


class NoticeAdmin(ModelAdmin):
    list_display = ['subject', 'cr_date']
    search_fields = ['cr_date']
    list_filter = ['subject', 'cr_date', 'msg']


class BranchAdmin(ModelAdmin):
    list_display = ['name', 'hod']


admin.site.register(Notice, NoticeAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Profile)