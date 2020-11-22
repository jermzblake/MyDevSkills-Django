from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.skill_index, name='index'),
    path('skill/<int:skill_id>/', views.skill_detail, name='detail'),
    path('skill/create/', views.SkillCreate.as_view(), name='skills_create'),
    path('skill/<int:pk>/update', views.SkillUpdate.as_view(), name='skills_update'),
    path('skill/<int:pk>/delete/', views.SkillDelete.as_view(), name='skills_delete'),
    path('skill/<int:skill_id>/add_note', views.add_note, name='add_note'),
    path('skill/<int:skill_id>/note/<int:pk>/delete/', views.NoteDelete.as_view(), name='notes_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    
]