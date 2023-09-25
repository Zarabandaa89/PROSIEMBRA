from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import RegisterForm, formularioPqrs, formulariocitas
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            names = form.cleaned_data.get('names')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = names
            user.last_name = username
            user.save()
            
            login(request, user)
            
            messages.success(request, 'Registro exitoso. Porfavor, Inice sesión.')
            
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form
    })


def register_login(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            names = form.cleaned_data.get('names')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = names
            user.last_name = username
            user.save()
            
            login(request, user)
            
            messages.success(request, 'Registro exitoso. Porfavor, Inice sesión.')
            
            return redirect('register')
    else:
        form = RegisterForm()

    return render(request, 'login.html', {
        'form': form
    })



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            welcome_message = f'Bienvenido, {user}!'
            #messages.success(request, welcome_message)
            response = redirect('main')
            response.set_cookie('welcome_message', welcome_message)
            return response
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'login.html', {

    })
    
    


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            names = form.cleaned_data.get('names')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = names
            user.last_name = username
            user.save()
            
            login(request, user)
            
            messages.success(request, 'Registro exitoso. Porfavor, Inice sesión.')
            
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form
    })



@login_required(login_url='login')
def products_view(request):
    return render(request, 'products.html')




@login_required(login_url='login')
def profile_view(request):
    return render(request, 'profile.html')






@login_required(login_url='login')
def customer_service_view(request):
    
    contact_form = formularioPqrs()
    
    if request.method == 'POST':
        contact_form = formularioPqrs(data=request.POST)
        
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Hemos recibido tu PQRS y estamos trabajando en ello. Te responderemos pronto. Gracias.')
            return redirect('customer')
        else:
            messages.error(request, '')
    return render(request, 'customer_service.html', {'form':contact_form})







@login_required(login_url='login')
def main_view(request):
    return render(request, 'main.html')






@login_required(login_url='login')
def we_view(request):
    return render(request, 'we.html')




@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada Gracias por visitarnos')
    return redirect('login')






@login_required(login_url='login')
def quotes_view(request):
    contact_form = formulariocitas()
    
    if request.method == 'POST':
        contact_form = formulariocitas(data=request.POST)
        
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request,'Tu cita ha sido registrada con éxito. Por favor, espera nuestra confirmación por correo electrónico. Gracias.')
            return redirect('quotes')
        
        else:
            messages.error(request, '')
    return render(request, 'quotes.html', {'form':contact_form})



def inicio_view(request):
    return render(request, 'inicio.html')