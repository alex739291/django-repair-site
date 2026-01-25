from django.db import models
from django.urls import reverse
import os

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nome del servizio")
    slug = models.SlugField(unique=True, verbose_name="URL", null=True, blank=True)
    description = models.TextField(verbose_name="Descrizione del servizio", blank=True)
    price = models.CharField(max_length=50, verbose_name="Prezzo", default="a partire da 50€")
    image = models.ImageField(upload_to='services/', verbose_name="Immagine del servizio")
    def get_webp_url(self):
        return os.path.splitext(self.image.url)[0] + '.webp'
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Servizio"
        verbose_name_plural = "Servizi"
    def get_absolute_url(self):
        # 'service_detail' — это имя (name) пути из твоего файла pages/urls.py
        return reverse('service_detail', kwargs={'slug': self.slug})    

class Order(models.Model):
    # Связываем заказ с конкретной услугой (если услугу удалят, заказ останется)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, verbose_name="Servizio")
    message = models.TextField(blank=True, null=True)
    
    name = models.CharField(max_length=100, verbose_name="Nome")
    phone = models.CharField(max_length=20, verbose_name="Telefono")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data richiesta")

    def __str__(self):
        return f"Ordine di {self.name} ({self.service})"

    class Meta:
        verbose_name = "Ordine"
        verbose_name_plural = "Ordini"

class Brand(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nome del marchio")
    logo = models.FileField(upload_to='brands/', verbose_name="Logo del marchio")
    image = models.ImageField(upload_to='brands/', verbose_name="Immagine del marchio")
    description = models.TextField(verbose_name="Descrizione del marchio", blank=True)
    slug = models.SlugField(unique=True, verbose_name="URL")
    def get_webp_url(self):
        if self.image:
            return os.path.splitext(self.image.url)[0] + '.webp'
        return ''

    def get_webp_logo_url(self):
        if self.logo:
            return os.path.splitext(self.logo.url)[0] + '.webp'
        return ''

    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse('brand_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = "Marchio"
        verbose_name_plural = "Marchi"
