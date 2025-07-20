from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash_screen, name='splash'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),  # 👈 ADD THIS LINE if missing
]
