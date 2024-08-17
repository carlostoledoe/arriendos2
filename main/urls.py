from django.urls import path
from main.views import index, register, profile
	
urlpatterns = [
    path('', index, name='index'),
    path('accounts/register/', register, name='register',),
    path('accounts/profile/', profile, name='profile',),
]