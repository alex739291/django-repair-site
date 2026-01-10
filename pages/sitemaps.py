from django.contrib.sitemaps import Sitemap
from .models import Service

class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Service.objects.all()

    def lastmod(self, obj):
        # Здесь мы могли бы возвращать дату обновления, если бы она была в модели.
        # Пока оставим просто obj (или можно добавить поле updated_at в модель)
        return None