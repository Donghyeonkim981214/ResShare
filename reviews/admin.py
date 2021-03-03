from django.contrib import admin
from . import models

@admin.register(models.Review)
class RestaurantAdmin(admin.ModelAdmin):
    pass