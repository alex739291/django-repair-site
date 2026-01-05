from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Order
from .forms import OrderForm
from django.contrib import messages
import requests
# Create your views here.
def home(request):
    services = Service.objects.all()
    return render(request, "pages/index.html", {"services": services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    
    # Если клиент отправил заполненную форму (нажал кнопку)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Создаем заказ, но пока не сохраняем в базу (commit=False)
            order = form.save(commit=False)
            # Прикрепляем к заказу текущую услугу (например, Холодильник)
            order.service = service
            # Теперь сохраняем окончательно
            order.save()
            # Показываем страницу с сообщением об успехе
            return render(request, 'pages/service_detail.html', {'service': service, 'success': True})
    
    # Если клиент просто зашел на страницу
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
        full_text = f"🔥 Новый заказ!\n👤 Имя: {name}\n📞 Тел: {phone}\n📝 Сообщение: {message}"
        send_telegram(full_text)
        messages.success(request, 'La tua richiesta è stata inviata con successo! Ti richiameremo presto.')

        # 3. Перенаправляем на главную (можно добавить сообщение об успехе)
        return redirect('home')

    return render(request, 'pages/contact.html')

def send_telegram(message):
    api_token = '7027717251:AAGhkPZDl8TQcmyCSiEkiMfAt27TFlAZSj8'  # Вставьте ваш длинный токен
    chat_id = '7429680555'  # Вставьте ваш номер ID

    url = f'https://api.telegram.org/bot{api_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}

    try:
        requests.post(url, data=data)
    except:
        print("Ошибка отправки в Telegram") # Чтобы сайт не сломался, если нет интернета    