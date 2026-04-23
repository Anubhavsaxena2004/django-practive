from . import views
from django.urls import path

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle, name='toggle_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('filter/', views.filter, name='filter'),
    path('mark_all/', views.mark_all, name='mark_all'),
    path('overdue/', views.overdue, name='overdue'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('v1/events/', views.events, name='events'),
]
