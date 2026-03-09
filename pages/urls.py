from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('service/<slug:slug>/', views.service_detail, name='service_detail'),
    path('contact/', views.contact_page, name='contact'),
    path('assistenza-<slug:slug>/', views.city_detail, name='city_detail'),
    path('assistenza-<slug:city_slug>/<slug:service_slug>/', views.city_service_detail, name='city_service_detail'),
    path('robots.txt', TemplateView.as_view(template_name='pages/robots.txt', content_type='text/plain')),
    path('privacy/', views.privacy, name='privacy'),
    path('brand/<slug:slug>/', views.brand_detail, name='brand_detail'),
    path('thanks/', views.thanks, name='thanks'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.article_detail, name='article_detail'),
]