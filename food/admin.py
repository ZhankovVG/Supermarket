from django.contrib import admin
from .models import *


@admin.register(Category)
# Категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')


class CommentsInline(admin.StackedInline):
    model = Comments
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Manufacturer)
# Производитель
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    list_display_links = ('name',)


@admin.register(Product)
# Продукты
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'price', 'weight', 'photo', 'draft', 'url')
    list_display_links = ('title',)
    list_filter = ('title', 'price')
    search_fields = ('title', 'category__name')
    list_editable = ('draft',)
    inlines = [CommentsInline]


@admin.register(RetingsStar)
# Звезда рейтинга
class RetingsStarAdmin(admin.ModelAdmin):
    list_display = ('value',)
    list_display_links = ('value',)


@admin.register(Comments)
# Коментарий
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'email')
    list_display_links = ('name',)
    readonly_fields = ('name', 'email')