from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nome del servizio")
    description = models.TextField(verbose_name="Descrizione del servizio", blank=True)
    price = models.CharField(max_length=50, verbose_name="Prezzo", default="a partire da 50€")
    image = models.ImageField(upload_to='services/', verbose_name="Immagine del servizio")
    
    # Эта функция нужна, чтобы в админке отображалось название, а не "Service object (1)"
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Servizio"
        verbose_name_plural = "Servizi"

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