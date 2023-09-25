from typing import Any
from django import forms
from django.contrib.auth.models import User 
from core.models import Customer_Service
from core.models import Rendezvous

class RegisterForm(forms.Form):
    name = forms.CharField(required=True, label='Nombre completo')
    username = forms.CharField(required=True, label='Nombre de usuario')
    email = forms.EmailField(required=True, label='Correo electronico' )
    password = forms.CharField(required=True, max_length=10, widget=forms.PasswordInput, label='Contraseña')
    confirm_password = forms.CharField (required=True, max_length=10, widget=forms.PasswordInput, label='Confirmar contraseña')

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')

        return username      

    def clean_email(self):
            email = self.cleaned_data.get('email')

            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('El email ya se encuentra en uso')

            return email    
    

class formularioPqrs(forms.ModelForm):
    application_date_pqrs = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha solicitud PQRS')
    class Meta:
        model = Customer_Service
        fields = ['application_date_pqrs','email','type_pqrs','description']
    
        
class formulariocitas(forms.ModelForm):
    date_time = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha de cita')
    
    class Meta:
        model = Rendezvous
        fields = ['date_time', 'email', 'virtual_onsite', 'location', 'appointment_type']