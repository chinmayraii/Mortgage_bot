from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('chatbot', views.chatbot, name='chatbot'),
]