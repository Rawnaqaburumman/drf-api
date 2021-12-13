from django.contrib import admin
from .models import Flowers


@admin.register(Flowers)
class FlowersAdmin(admin.ModelAdmin):
    list_display = ['name','description','user']
