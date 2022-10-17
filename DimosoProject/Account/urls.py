
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signin2', views.signin2, name='signin2'),
    
    path('logout', views.logout, name='logout'),
    
]