from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

from django.contrib.auth.views import LoginView,LogoutView

app_name = 'app_users'

urlpatterns = [
    path('',views.indexView,name="home"),
    path('dashboard/', views.dashboardView, name="dashboard_url"),
    # path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)