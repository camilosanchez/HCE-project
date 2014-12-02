from django.contrib import admin
from .models import EventActivity, ExtraActivity, Interest, ExtraCustom, ActivityAssist, ExtraRegistration

admin.site.register(EventActivity)
admin.site.register(ExtraActivity)
admin.site.register(Interest)
admin.site.register(ExtraCustom)
admin.site.register(ActivityAssist)
admin.site.register(ExtraRegistration)
