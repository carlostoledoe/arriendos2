from django.urls import path
from main.views import index, register
	
urlpatterns = [
    path('', index, name='index'),
    path('accounts/register/', register, name='register',),
]