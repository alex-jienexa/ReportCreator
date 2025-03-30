from django.urls import path
from .views import users

urlpatterns = [
    path('login/', users.login_view, name='login'),
    path('csrf/', users.get_csrf_token, name='csrf_token'),
    path('check_auth/', users.check_auth, name='check_auth'),
]
