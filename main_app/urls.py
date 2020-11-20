from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.skill_index, name='index'),
    path('skill/<int:skill_id>/', views.skill_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    
]