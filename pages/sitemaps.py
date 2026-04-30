from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Service, Brand, Article, City

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

class BrandSitemap(Sitemap):
    protocol = 'https'
    priority = 0.7
    changefreq = 'monthly'

    def items(self):
        return Brand.objects.all()

class ArticleSitemap(Sitemap):
    protocol = 'https'
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return Article.objects.all()

class CitySitemap(Sitemap):
    protocol = 'https'
    changefreq = "weekly"
    priority = 0.8

    def items(self): 
        return City.objects.filter(is_major_city=True)

    def location(self, obj): 
        return reverse('city_detail', args=[obj.slug])

class CityServiceSitemap(Sitemap):
    protocol = 'https'
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        items_list = []
        for city in City.objects.filter(is_major_city=True).prefetch_related('services'):
            for service in city.services.all():
                items_list.append({'city': city, 'service': service})
        return items_list

    def location(self, obj): 
        return reverse('city_service_detail', kwargs={'city_slug': obj['city'].slug, 'service_slug': obj['service'].slug})