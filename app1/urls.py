from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.first, name='first'),
    path('<int:tech_id>', views.detail, name='detail'),
]
