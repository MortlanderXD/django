
from django.urls import path, include 
from . import views

app_name = "members"

urlpatterns = [
    
    path('', views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    
    path('login/', views.login_view, name="login"),
    
    path('logout/', views.logout_view, name="logout"),
    
]

