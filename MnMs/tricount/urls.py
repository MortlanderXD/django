from django.urls import path 
from . import views

app_name = "tricount"

urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.loginView,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('account/', views.account,name="account"),
    #path('welcome/', views.index,name='index'),
    
]
