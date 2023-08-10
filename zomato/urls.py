from django.urls import path
from . import views

app_name = 'zomato'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add/', views.add, name='add'),
    path('listuser/', views.user_list, name='user-list'),
    path('edit/<int:user_id>/', views.edit_user, name='edit-user'),  # Add this line
    path('set-editing/', views.set_editing, name='set-editing'),
    path('confirm-edit/<int:user_id>/', views.confirm_edit, name='confirm-edit'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete-user'),
    # Add other URL patterns as needed
]
