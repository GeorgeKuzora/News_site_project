from django.urls import path
from app_users.views import login_view, logout_view
from app_users.views import AnotherLoginView, UserRegisterView, UserEditView


urlpatterns = [
        path('login/', login_view, name='login'),
        path('another_login/', AnotherLoginView.as_view(), name='another_login'),
        path('logout/', logout_view, name='logout'),
        path('register/', UserRegisterView.as_view(), name='register'),
        path('edit/', UserEditView.as_view(), name='edit'),
        ]
