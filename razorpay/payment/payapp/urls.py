from django.urls import path
from payapp import views

urlpatterns = [
    path('', views.index),
    path('success/', views.success),
]
