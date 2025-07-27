from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls')),  # ← cambia esto por el nombre correcto de tu app
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
   

]