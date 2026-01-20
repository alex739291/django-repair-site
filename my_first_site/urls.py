"""
URL configuration for my_first_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView  # Нужно для robots.txt

# Импортируем оба класса карты сайта
from pages.sitemaps import ServiceSitemap, StaticViewSitemap 

# Объединяем статику и услуги в одну карту
sitemaps = {
    'static': StaticViewSitemap,
    'services': ServiceSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    
    # 1. Карта сайта (Sitemap)
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, 
         name='django.contrib.sitemaps.views.sitemap'),
    
    # 2. Robots.txt (Важно: указываем путь к шаблону внутри папки pages)
    path('robots.txt', TemplateView.as_view(
        template_name="pages/robots.txt", 
        content_type="text/plain"
    )),
]

# Для работы картинок в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)