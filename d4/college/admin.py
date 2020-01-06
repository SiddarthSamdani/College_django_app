from django.contrib import admin
from .models import Notice
from django.contrib.admin.options import ModelAdmin
from .models import Branch, Profile, Question


class NoticeAdmin(ModelAdmin):
    list_display = ['subject', 'cr_date']
    search_fields = ['cr_date']
    list_filter = ['subject', 'cr_date', 'msg']


class BranchAdmin(ModelAdmin):
    list_display = ['name', 'hod']


admin.site.register(Notice, NoticeAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Profile)


class QuestionAdmin(ModelAdmin):
    list_display = ['subject', 'cr_date']
    search_fields = ['cr_date']
    list_filter = ['subject', 'cr_date', 'msg']


admin.site.register(Question, QuestionAdmin)