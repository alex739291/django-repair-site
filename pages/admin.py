from django.contrib import admin
from .models import Order, Service, Brand, Article, City    
admin.site.register(City)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'meta_description')
    fields = ('title', 'slug', 'logo', 'image', 'description', 'meta_description', 'seo_text')
    prepopulated_fields = {'slug': ('title',)}

# 2. Регистрируем Заказы с красивой таблицей (это заменяет старую строку)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message', 'created_at') # Колонки
    search_fields = ('name', 'phone')  # Поиск
    list_filter = ('created_at',)      # Фильтр справа

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    # Автозаполнение поля slug из поля title
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'short_description')   
    filter_horizontal = ('brands',) 

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}