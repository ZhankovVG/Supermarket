from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Category)
# Категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')
    prepopulated_fields = {'url' : ('name',)}


class CommentsInline(admin.StackedInline):
    model = Comments
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Manufacturer)
# Производитель
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'get_image')
    list_display_links = ('name',)
    readonly_fields = ('image',)

    def get_image(self, objects):
        return mark_safe(f"<img src={objects.image.url} width='50' ")
    
    get_image.short_description = 'Изображение'


@admin.register(Product)
# Продукты
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'price', 'weight', 'get_photo', 'draft', 'url')
    list_display_links = ('title',)
    list_filter = ('title', 'price')
    search_fields = ('title', 'category__name')
    list_editable = ('draft',)
    inlines = [CommentsInline]
    readonly_fields = ('photo',)

    def get_photo(self, objects):
        return mark_safe(f"<img src={objects.photo.url} width='50' ")
    
    get_photo.short_description = 'Изображение'

    prepopulated_fields = {'url' : ('title',)}


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