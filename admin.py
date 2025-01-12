from django.contrib import admin

# Register your models here.
from.models import*

admin.site.register(registrationmodel)
admin.site.register(spammodel)
admin.site.register(reportmodel)
admin.site.register(feedmodel)


