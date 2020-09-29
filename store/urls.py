from django.contrib import admin
from django.urls import path
from .views.home import  store
from .views.signup import Signup
from .views.login import Login , logout
from .views.crud import Crud 


urlpatterns = [
    path('store', store , name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('crud',Crud.as_view(),name='crud'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),

]
