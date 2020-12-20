from django.urls import path
from . import views


user_list = views.UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('', views.hello_world),
    path('users/', user_list, name='user-list'),
    path('users/<username>/', user_detail, name='user-detail')
]
