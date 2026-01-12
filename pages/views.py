from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Order, Brand
from .forms import OrderForm
from django.contrib import messages
import requests

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            message_text = f"🔥 Nuovo contatto dalla Home!\n👤 Nome: {order.name}\n📞 Tel: {order.phone}"

            send_telegram(message_text)
            
            messages.success(request, 'Grazie! Ti richiameremo entro 15 minuti.')
            # ИЗМЕНЕНО: теперь перенаправляем на страницу благодарности
            return redirect('thanks')
    
    services = Service.objects.all()
    brands = Brand.objects.all()
    context = {
        "services": services,
        "brands": brands
    }
    
    return render(request, "pages/index.html", context)

def service_detail(request, pk):
    # Находим услугу по ID (например, Холодильник)
    service = get_object_or_404(Service, pk=pk)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        
        if form.is_valid():
            order = form.save()
            # Можно уточнить в сообщении, какая именно услуга заказана
            message_text = f"🔥 Nuovo contatto per {service.title}!\n👤 Nome: {order.name}\n📞 Tel: {order.phone}"

            send_telegram(message_text)
            
            messages.success(request, 'Grazie! La tua richiesta è stata inviata. Ti richiameremo a breve.')
            
            # ИЗМЕНЕНО: теперь перенаправляем на страницу благодарности
            return redirect('thanks')
            
    else:
        form = OrderForm()

    return render(request, 'pages/service_detail.html', {'service': service, 'form': form})

def contact_page(request):
    if request.method == 'POST':
        # 1. Получаем данные из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # 2. Создаем заказ в базе данных
        Order.objects.create(
            name=name, 
            phone=phone,
            message=message
        )
        full_text = f"🔥 Новый заказ (страница контактов)!\n👤 Имя: {name}\n📞 Тел: {phone}\n📝 Сообщение: {message}"
        send_telegram(full_text)
        messages.success(request, 'La tua richiesta è stata inviata con successo! Ti richiameremo presto.')

        # ИЗМЕНЕНО: теперь перенаправляем на страницу благодарности
        return redirect('thanks')

    return render(request, 'pages/contact.html')

def send_telegram(message):
    api_token = '7027717251:AAGhkPZDl8TQcmyCSiEkiMfAt27TFlAZSj8'
    chat_id = '7429680555'

    url = f'https://api.telegram.org/bot{api_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}

    try:
        requests.post(url, data=data, timeout=5)
    except:
        print("Errore di invio Telegram") 
        
def privacy(request):
    return render(request, 'pages/privacy.html')       


def brand_detail(request, slug):
    brand = get_object_or_404(Brand, slug=slug)
    
    context = {
        'brand': brand
    }
    return render(request, 'pages/brand_detail.html', context)

# Страница благодарности
def thanks(request):
    return render(request, 'pages/thanks.html')