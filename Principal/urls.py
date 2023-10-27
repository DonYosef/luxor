from django.urls import path
from .views import home, login, register, profile, table

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'), 
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('table/', table, name='table'),
]