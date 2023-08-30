from django.urls import path
from .views import (
    UserRegisterView,
    UserLoginView,
    UserDetailView,
    UserListView,
    UserUpdateView,
    UserDeleteView,
    HealthCheckView,
)
app_name = 'api'
urlpatterns = [
    path('api/users/register', UserRegisterView.as_view(), name='user_register'),
    path('api/auth/login', UserLoginView.as_view(), name='user_login'),
    path('api/users/<int:user_id>', UserDetailView.as_view(), name='user_detail'),
    path('api/users/all', UserListView.as_view(), name='user_list'),
    path('api/users/<int:user_id>/update', UserUpdateView.as_view(), name='user_update'),
    path('api/users/<int:user_id>/delete', UserDeleteView.as_view(), name='user_delete'),
    path('api/health-check', HealthCheckView.as_view(), name='health-check'),
]
