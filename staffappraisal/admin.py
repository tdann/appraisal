from django.contrib import admin
from .models import (
    Faculty,
    Profile,
    AppraiseeComment,
    AppraiserAndAppraiseeAgreement,
    Competence,
    OverallPerformance,
    Performance,
    AppraiserComment,
    VcComment,
    Department
)

class AppraiserAndAppraiseeAgreementAdmin(admin.ModelAdmin):
    list_display=['competence', 'key_outputs', 'self_rating', 'supervisor_rating', 'agreed_rating']
    list_filter=['self_rating', 'supervisor_rating']

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Profile)
admin.site.register(AppraiseeComment)
admin.site.register(AppraiserAndAppraiseeAgreement, AppraiserAndAppraiseeAgreementAdmin)
admin.site.register(OverallPerformance)
admin.site.register(Performance)
admin.site.register(Competence)
admin.site.register(VcComment)
admin.site.register(Department)
admin.site.register(AppraiserComment)