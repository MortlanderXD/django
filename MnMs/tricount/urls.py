from django.urls import path 
from . import views

app_name = "tricount"

urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.loginView,name='login'),
    #path('logout/', views.logout,name='logout'),
    #path('welcome/', views.index,name='index'),
    
]
