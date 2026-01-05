from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('service/<int:pk>', views.service_detail, name='service_detail'),
    path('contact/', views.contact_page, name='contact'),
    path('robots.txt', TemplateView.as_view(template_name='pages/robots.txt', content_type='text/plain')),
]