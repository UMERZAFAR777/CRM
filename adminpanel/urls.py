from django.contrib import admin
from django.urls import path,include
from adminpanel import views


urlpatterns = [
    path('', views.admin_login , name='admin_login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.admin_logout,name='admin_logout'),
    path('edit-student/<id>',views.edit_student,name='edit_student'),
    path('delete-student/<id>',views.delete_student,name='delete_student'),
    
]
