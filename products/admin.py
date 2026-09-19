from django.contrib import admin
from .models import Category, Company, Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'is_active',)
    list_filter  = ('company' ,'name')


admin.site.register(Category, CategoryAdmin)

class ComponyAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active',)
    list_filter  = ('name',)

admin.site.register(Company, ComponyAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('company', 'category', 'name', 'price', 'is_active')
    list_filter  = ('company', 'category', 'price', 'is_active')

admin.site.register(Product, ProductAdmin)