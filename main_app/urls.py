from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.skill_index, name='index'),
    path('skill/<int:skill_id>/', views.skill_detail, name='detail'),
    path('skill/create/', views.SkillCreate.as_view(), name='skills_create'),
    path('accounts/signup/', views.signup, name='signup'),
    
]