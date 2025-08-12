from django.contrib import admin
from django.urls import path, include
from accounts import views as acc_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', acc_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', acc_views.dashboard, name='dashboard'),
    path('deposit/', acc_views.deposit, name='deposit'),
    path('withdraw/', acc_views.withdraw, name='withdraw'),
]
