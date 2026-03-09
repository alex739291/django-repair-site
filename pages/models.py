from django.db import models
from django.urls import reverse
import os

class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome della città")
    slug = models.SlugField(unique=True, verbose_name="URL")
    map_iframe = models.TextField(blank=True, verbose_name="Mappa Google (iframe)")
    description = models.TextField(blank=True, verbose_name="Descrizione SEO")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Città"
        verbose_name_plural = "Città"

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nome del servizio")
    slug = models.SlugField(unique=True, verbose_name="URL", null=True, blank=True)
    description = models.TextField(verbose_name="Descrizione del servizio", blank=True)
    short_description = models.TextField(blank=True, max_length=200, verbose_name="Descrizione Breve")

    image = models.ImageField(upload_to='services/', verbose_name="Immagine del servizio")
    brands = models.ManyToManyField('Brand', related_name="services", blank=True, verbose_name="Marchi associati")
    cities = models.ManyToManyField(City, related_name='services', blank=True, verbose_name="Città servite")
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
    meta_description = models.CharField(max_length=160, blank=True, verbose_name="Meta Description (SEO)")
    seo_text = models.TextField(blank=True, verbose_name="Testo SEO (vsc)")
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

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titolo")
    slug = models.SlugField(unique=True, verbose_name="URL")
    image = models.ImageField(upload_to='blog/', verbose_name="Immagine")
    short_description = models.TextField(max_length=300, verbose_name="Breve descrizione")
    content = models.TextField(verbose_name="Contenuto completo")
    meta_description = models.CharField(max_length=160, blank=True, verbose_name="Meta Description (SEO)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data di creazione")
    related_service = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True, blank=True, related_name='articles', verbose_name="Servizio correlato")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"
        ordering = ['-created_at']
