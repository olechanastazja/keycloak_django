from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello_world),
    path('user_exists/', views.user_exists),
    path('create_user/', views.create_user),
]
