from django.contrib import admin
from django.urls import path, include

from app_users import views

urlpatterns = [
    path('',include('app_users.urls')),        
    path('register_please/', views.registerPleaseView, name="registration_url"),
    path('login_please/', views.loginPleaseView, name="signin_url"),
    path('stocks/', include('app_stock_indices.urls')),        
    path('admin/', admin.site.urls),
]
