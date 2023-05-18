from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('mortgage_chatbot', views.mortgage_chatbot, name='mortgage_chatbot'),
]