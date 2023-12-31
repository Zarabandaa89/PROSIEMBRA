from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('', views.inicio_view, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('login/register.html', views.register, name= 'login a registro'),
    path('login/login', views.login_view),
    path('register/register', views.register, name='register'),
    path('register/login', views.login_view, name='login'),
    path('register/register.htmls', views.register_view, name='register'),
    path('register/password_reset_form.html', views.password_reset_view, name='password'),
    path('login/register.htmls', views.register),
    path('products/', views.products_view, name='products'),
    path('profile/', views.profile_view, name='profile'),
    path('customer_service', views.customer_service_view, name='customer'),
    path('main/', views.main_view, name='main'),
    path('we/', views.we_view, name='we'),
    path('logout/', views.logout_view, name='logout'),
    path('quotes/', views.quotes_view, name='quotes'),
    path('consultas/', views.consultas_view, name='consultas'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)