from django.urls import path

from . import views

urlpatterns = [

    path('', views.abcd, name='abcd'),
    # path('add/', views.addition,name='addition')

]

