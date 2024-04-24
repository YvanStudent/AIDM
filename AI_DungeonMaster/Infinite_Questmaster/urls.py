from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.about, name='about'),
    path('', views.loginpage, name='login'),
    path('', views.signuppage, name='signup'),
    path('', views.account1, name='account1'),
    path('', views.account2, name='account2'),
    path('', views.account3, name='account3'),    
    path('', views.feedback, name='feedback'),
    path('', views.chatbot, name='chatbot'),
]