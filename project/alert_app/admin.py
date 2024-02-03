from django.contrib import admin
# Register your models here.

from .models import User, Alert

class ReadOnlyFields(admin.ModelAdmin):
    readonly_fields = ['username', 'email', 'password']

admin.site.register(User, ReadOnlyFields)
admin.site.register(Alert)