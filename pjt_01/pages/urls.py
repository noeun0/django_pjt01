from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('create/', views.create, name='create')
]
