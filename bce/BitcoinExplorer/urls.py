from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('BlockExplorer/', views.blockExplorer, name='be')
]