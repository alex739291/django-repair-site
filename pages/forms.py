from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone']
        # Добавляем стили (CSS классы), чтобы форма была красивой
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Il tuo nome'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Il tuo numero'}),
        }