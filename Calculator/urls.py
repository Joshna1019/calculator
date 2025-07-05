from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'), 
    path('Hello/',views.Hello,name='Hello')
]
