from django.contrib import admin
from .models import Order, Service  # Импортируем обе модели

# 1. Просто регистрируем Услуги (как и было)
admin.site.register(Service)

# 2. Регистрируем Заказы с красивой таблицей (это заменяет старую строку)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message', 'created_at') # Колонки
    search_fields = ('name', 'phone')  # Поиск
    list_filter = ('created_at',)      # Фильтр справа