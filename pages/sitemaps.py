from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Service

# Карта для статических страниц (Главная)
class StaticViewSitemap(Sitemap):
    protocol = 'https'
    priority = 1.0        # Максимальный приоритет
    changefreq = 'monthly' # Как часто обновляется контент

    def items(self):
        # Здесь указываем 'home', так как это имя (name) пути в pages/urls.py
        return ['home']

    def location(self, item):
        return reverse(item)

# Карта для динамических страниц (Услуги: ремонт стиральных машин и т.д.)
class ServiceSitemap(Sitemap):
    protocol = 'https'
    priority = 0.8        # Высокий приоритет для страниц услуг
    changefreq = 'weekly'  # Услуги могут обновляться чаще

    def items(self):
        # Берем все услуги из базы данных
        return Service.objects.all()

    # Django автоматически будет искать метод get_absolute_url в модели Service