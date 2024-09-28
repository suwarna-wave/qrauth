from django.contrib import admin
from .models import ScannedQR

class ScannedQRAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'role', 'created_at')  # Add fields you want to display
    list_filter = ('country', 'role', 'created_at')  # Add fields you want to filter by

admin.site.register(ScannedQR, ScannedQRAdmin)