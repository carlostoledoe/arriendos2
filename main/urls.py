from django.urls import path
from main.views import index, register, profile, change_pass, add_propiedad, edit_propiedad, delete_propiedad
	
urlpatterns = [
    path('', index, name='index'),
    path('accounts/register/', register, name='register',),
    path('accounts/profile/', profile, name='profile',),
    path('accounts/change-pass/', change_pass, name='change_pass',),
    path('propiedad/add-propiedad/', add_propiedad, name='add_propiedad',),
    path('propiedad/edit-propiedad/<id>', edit_propiedad, name='edit_propiedad',),
    path('propiedad/delete-propiedad/<id>', delete_propiedad, name='delete_propiedad',),
]