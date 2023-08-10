from django.urls import path
from . import views

app_name = 'Basic'

urlpatterns = [
    path('enter/<str:username>/', views.enter, name='enter'),
    path('leave/<str:username>/', views.leave, name='leave'),
    # Add other URL patterns as needed
]
