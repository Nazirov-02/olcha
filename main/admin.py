from django.contrib import admin
from main.models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','section']

@admin.register(Category)
class Admin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name','category']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','product']

@admin.register(Characteristic)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['name','value']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['product']
