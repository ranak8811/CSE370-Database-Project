from django.contrib import admin
from django.urls import path
from authentication import views



urlpatterns = [
    path('', views.handlelogin, name = ''),
    path('logout', views.handlelogout, name = 'logout'),
    path('signup', views.signup, name = 'signup'),
    path('add_task', views.add_task, name = 'add_task'),
    path('all_tasks/', views.all_tasks, name = 'all_tasks'),
    path('delete_todo/<int:id>/', views.delete_todo, name='delete_todo'),
    path('change_status/pending/<int:id>/', views.change_status_pending, name='change_status'),
    path('change_status/completed/<int:id>/', views.change_status_completed, name='change_status'),
    path('wk/', views.weekly_task, name = 'week'),
    path('mn/', views.monthly_task, name = 'month'),
    path('cmp/', views.completed_tasks, name = 'completed'),
    path('team/', views.team, name = 'team'),
    path('teamdash/', views.teamdash, name = 'teamdash'),
    path('user/', views.user, name = 'user'),
    path('idx/', views.index, name= 'index'),
]

