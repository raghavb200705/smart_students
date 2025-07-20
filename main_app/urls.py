from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash_screen, name='splash'),
    path('login/', views.login_view, name='login'),
    path('home/', views.splash_screen, name='home'),  # Temporarily show splash on home
]
