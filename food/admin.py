from django.contrib import admin
from .models import *


@admin.register(Category)
# Категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')
    list_display_links = ('name',)